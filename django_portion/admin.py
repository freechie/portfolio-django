from django.contrib import admin
from .models import Project, Skill, Post, Comment, Resume, ProjectImage

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
    approve_comments.short_description = "Mark selected comments as approved up on review"

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'is_featured', 'created_at', 'updated_at')
    list_filter = ('status', 'is_featured', 'created_at', 'updated_at')
    search_fields = ('title', 'description', 'technologies')

@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ['project', 'caption']
    list_filter = ['project']

admin.site.register(Skill)
admin.site.register(Post)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Resume)
