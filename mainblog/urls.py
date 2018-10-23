from django.urls import path
from . import views
from mainblog.views import ArchiveListView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create_post/', views.create_post, name='create_post'),
    path('blog_post/<int:post_id>/', views.blog_post, name='blog_post'),
    path('edit_post/<int:post_id>/edit', views.edit_post, name='edit_post'),
    path('archive_post/<int:post_id>', views.archived_post, name='archived_post'),
    path('category_page/<slug:slug>/', views.category_page, name='category_page'),
    path('archive_list/', ArchiveListView.as_view(), name='archive_list'),
    path('tag_page/<int:tag_id>/', views.tag_page, name='tag_page'),
    path('blog_post/<int:post_id>/draft/', views.draft_post, name='draft_post'),

]
