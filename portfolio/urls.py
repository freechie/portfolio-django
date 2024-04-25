from django.contrib import admin
from django.urls import path, re_path, include
from django_portion import views
from rest_framework.routers import DefaultRouter
from django_portion.views import ProjectViewSet
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.http import HttpResponse

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("blog/", views.blog_index, name="blog_index"),
    path("blog/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("about/", views.about_me, name="about_me"),
    path("skills/", views.skills_index, name="skills_index"),
    path("resume/", views.resume, name="resume"),
    path("contact/", views.contact, name="contact"),
    path("api/", include(router.urls)),
    path("tag/<str:tag_name>/", views.blog_by_tag, name='blog_by_tag'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path("__reload__/", include("django_browser_reload.urls")),
    path("__debug__/", include("debug_toolbar.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
