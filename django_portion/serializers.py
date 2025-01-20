from rest_framework import serializers
from .models import Project, ProjectImage
from taggit.models import Tag

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super().__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

class ProjectImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = ProjectImage
        fields = ['id', 'image', 'caption']


    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and request is not None:
            return request.build_absolute_uri(obj.image.url)
        return obj.image.url


class ProjectSerializer(DynamicFieldsModelSerializer):
    tags = serializers.SerializerMethodField()
    new_tags = serializers.ListField(write_only=True, required=False)
    images = ProjectImageSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'
        extra_kwargs = {
            'images': {'required': False, 'allow_null': True},
        }

    def get_tags(self, obj):
        return list(obj.tags.names())

    def validate_new_tags(self, value):
        if any(len(tag) > 20 for tag in value):
            raise serializers.ValidationError("Each tag must be no longer than 20 characters.")
        return value

    def create(self, validated_data):
        tags_data = validated_data.pop('new_tags', [])
        project = Project.objects.create(**validated_data)
        for tag_name in tags_data:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            project.tags.add(tag)
        return project

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('new_tags', None)
        project = super().update(instance, validated_data)
        if tags_data is not None:
            instance.tags.clear()
            for tag_name in tags_data:
                tag, _ = Tag.objects.get_or_create(name=tag_name)
                instance.tags.add(tag)
        return project

