from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from .validators import validate_file_size
from django.urls import reverse


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # General link, could be to a live version
    link = models.URLField(blank=True, null=True)
    repo_link = models.URLField(blank=True, verbose_name='Repository Link')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = TaggableManager()
    technologies = models.CharField(
        max_length=200, default="Not Specified", help_text="List technologies separated by commas")
    STATUS_CHOICES = (
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('archived', 'Archived'),
    )
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='in_progress')
    is_featured = models.BooleanField(
        default=False, help_text="Mark as featured to highlight on the portfolio")
    contribution_role = models.TextField(
        blank=True, help_text="Your role in the project")

    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=50)
    proficiency = models.IntegerField()

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80, default='Anonymous')
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class Resume(models.Model):
    title = models.CharField(max_length=100)
    upload = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='project_images/', validators=[validate_file_size])
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.project.title} - {self.caption[:20]}"
