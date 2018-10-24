from django.urls import path
from . import views
from mainblog.views import (
    ArchiveListView,
    IndexView,
    CreateView,
    BlogDetailView,
    EditView,
    ArchiveView,
    CategoryListView,
    TagView,
    DraftView,
    DraftListView
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create_post/', CreateView.as_view(), name='create_post'),
    path('blog_post/<int:id>/', BlogDetailView.as_view(), name='blog_post'),
    path('edit_post/<int:id>/edit', EditView.as_view(), name='edit_post'),
    path('archive_post/<int:id>', ArchiveView.as_view(), name='archived_post'),
    path('category_page/<slug:slug>/', CategoryListView.as_view(), name='category_page'),
    path('archive_list/', ArchiveListView.as_view(), name='archive_list'),
    path('tag_page/<int:id>/', TagView.as_view(), name='tag_page'),
    path('blog_post/<int:id>/draft/', DraftView.as_view(), name='draft_post'),
    path('draftlist/', DraftListView.as_view(), name='draft_list')

]
