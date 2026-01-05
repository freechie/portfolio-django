from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

from django_portion import views as django_portion_views
from rest_framework.routers import DefaultRouter
from django_portion.views import ProjectViewSet

# Wagtail URLs
from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

# API Router setup
router = DefaultRouter()
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    # Home Page
    path('', django_portion_views.index, name='index'),
    
    # Silence service-worker.js 404s
    path('service-worker.js', lambda r: HttpResponse("", content_type="application/javascript")),

    # Wagtail admin
    path('cms/', include(wagtailadmin_urls)),
    
    # Wagtail documents
    path('documents/', include(wagtaildocs_urls)),
    
    # Wagtail pages (serves /blog/ and other Wagtail content)
    path('blog/', include(wagtail_urls)),
    
    # React Frontend
    path('frontend/', include('frontend.urls')),
    
    # Portfolio views
    path('projects/', include('django_portion.urls')),
    path('posts/', django_portion_views.blog_index, name='blog_index'),
    path('posts/<int:pk>/', django_portion_views.blog_detail, name='blog_detail'),
    path('about/', django_portion_views.about_me, name='about_me'),
    path('skills/', django_portion_views.skills_index, name='skills_index'),
    path('resume/', django_portion_views.resume, name='resume'),
    path('contact/', django_portion_views.contact, name='contact'),
    
    # API and Third Party
    path('api/', include(router.urls)),
    path("__reload__/", include("django_browser_reload.urls")),
    path("captcha/", include("captcha.urls")),
    path('admin/', admin.site.urls),
]

# Media and Static files for development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)