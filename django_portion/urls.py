from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_index, name='project_index'),
    path('<int:pk>/', views.project_detail, name='project_detail'),
    path('tag/<str:tag_name>/', views.blog_by_tag, name='blog_by_tag'),
]

