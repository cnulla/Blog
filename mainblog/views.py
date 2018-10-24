from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
    reverse
)

from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Post, Category, Tag
from .forms import PostForm, TagForm
from django.contrib.auth.models import User
from django.views.generic import TemplateView, View


class IndexView(TemplateView):
    """ Display All Published Blogs of the user"""
    template_name = 'home.html'
    def get(self, *args, **kwargs):
        category = Category.objects.all()
        tags = Tag.objects.all()
        posts = Post.objects.filter(is_archived=False).order_by('-date_added')
        context = {'posts': posts, 'tags': tags, 'category': category}
        return render(self.request, self.template_name, context)


class CreateView(TemplateView):
    """ Create a blog """
    template_name = 'create_post.html'

    def get(self, *args, **kwargs):
        form = PostForm()
        return render(self.request, self.template_name, {'form': form})

    def post(self, *args, **kwargs):
        form = PostForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = self.request.user
            post.save()
            return HttpResponseRedirect(reverse('index'))


class BlogDetailView(TemplateView):
    """ Display the detail of the blog """
    template_name = 'blog_post.html'

    def get(self, *args, **kwargs):
        try:
            post = Post.objects.get(pk=kwargs.get('id'))
        except Post.DoesNotExist:
            raise Http404
        return render(self.request, self.template_name, {'post': post})


class EditView(TemplateView):
    """ Let the user edit his/her blog"""
    template_name = 'edit_post.html'

    def get(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs.get('id'), author=self.request.user)
        form = PostForm(instance=post)
        return render(self.request, self.template_name, {'post': post, 'form': form})

    def post(self, *args, **kwargs):
        form = PostForm(instance=post, data=self.request.POST)
        if form.is_valid():
            post.date_added = timezone.now()
            post.save()
            return HttpResponseRedirect(reverse('IndexView'))

class ArchiveListView(TemplateView):
    """ Display list of archive list
    """
    template_name = 'archive_list.html'

    def get(self, *args, **kwargs):
        archive = Post.objects.filter(is_archived=True)
        return render(self.request, self.template_name, {'archive': archive})

class ArchiveView(View):
    """ Option for users to archive the blog or not"""
    def get(self, *args, **kwargs):
        try:
            posts = Post.objects.get(pk=kwargs.get('id'), author=self.request.user)
            posts.is_archived = True
            posts.save()
        except Post.DoesNotExist:
            raise Http404
        return HttpResponseRedirect(reverse('archive_list'))


@login_required
def category_page(request, slug):
    # Display list of blog per cateory
    get_category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=get_category)
    return render(request, 'category_post.html', {'get_category': get_category,'posts': posts})


def tag_page(request, tag_id):
    tags = get_object_or_404(Tag, pk=tag_id)
    tag_post = Post.objects.filter(tag=tags.id)
    return render(request, 'tag_page.html', {'tags': tags, 'tag_post': tag_post})


def draft_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        is_draft = post.is_draft
        if is_draft == False:
            post.is_draft = True
            post.save()
            return redirect('blog_post', post_id=post.id)

        post.is_draft = False
        post.save()
        return redirect('blog_post', post_id=post.id)

