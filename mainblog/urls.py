from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_post/', views.create_post, name='create_post'),
    path('blog_post/<int:post_id>/', views.blog_post, name='blog_post'),
    path('edit_post/<int:post_id>/edit', views.edit_post, name='edit_post'),
    path('archive_post/<int:post_id>/archive', views.archive_post, name='archive_post')
    #path('', views.home, name='home'),
]

