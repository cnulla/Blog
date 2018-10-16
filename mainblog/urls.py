from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_post/', views.create_post, name='create_post'),
    path('blog_post/<int:post_id>/', views.blog_post, name='blog_post'),
    path('edit_post/<int:post_id>/edit', views.edit_post, name='edit_post'),
    path('archive_post/', views.archived_post, name='archived_post'),
    path('category_page/', views.category_page, name='category_page')
    #path('', views.home, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
