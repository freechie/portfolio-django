from rest_framework import serializers
from django.urls import reverse

from .models import Project, ProjectImage

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


class ProjectSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()
    images = ProjectImageSerializer(many=True, read_only=True)
    detail_url = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            'id',
            'title',
            'description',
            'contribution_role',
            'created_at',
            'updated_at',
            'status',
            'technologies',
            'tags',
            'images',
            'repo_link',
            'is_featured',
            'link',
            'detail_url',
        ]

    def get_tags(self, obj):
        return list(obj.tags.names())

    def get_detail_url(self, obj):
        path = reverse('project_detail', args=[obj.pk])
        request = self.context.get('request')
        return request.build_absolute_uri(path) if request else path
