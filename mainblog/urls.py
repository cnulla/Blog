from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_post/', views.create_post, name='create_post'),
    path('blog_post/<int:post_id>/', views.blog_post, name='blog_post'),
    path('edit_post/<int:post_id>/edit', views.edit_post, name='edit_post'),
    path('archive_post/<int:post_id>', views.archived_post, name='archived_post'),
    path('category_page/<int:category_id>/', views.category_page, name='category_page'),
    path('archive_list/', views.archive_list, name='archive_list')
]
