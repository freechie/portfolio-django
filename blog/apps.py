# blog/apps.py

from django.apps import AppConfig

class BlogConfig(AppConfig):
    default_auto_field = 'title'
    name = 'blog'
    verbose_name = 'Blog (Wagtail)'

