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

    template_name = 'home.html'
    def get(self, *args, **kwargs):
        category = Category.objects.all()
        tags = Tag.objects.all()
        posts = Post.objects.filter(is_archived=False).order_by('-date_added')
        context = {'posts': posts, 'tags': tags, 'category': category}
        return render(self.request, self.template_name, context)


@login_required
def create_post(request):
    form =  PostForm()
    # tag = TagForm()

    if request.method == 'POST':
        import pdb; pdb.set_trace()
        form = PostForm(request.POST, request.FILES)
        # tag = TagForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post, created = Post.objects.get_or_create(defaults__exact=tag)
            post.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            form = PostForm(request.POST)

    context = {'form': form}
    return render(request, 'create_post.html', context)


def blog_post(request, post_id):
    try:
        post = Post.objects.get(pk=post_id,author=request.user)
        tags = Post.objects.filter(tag=post.id)
    except Post.DoesNotExist:
        raise Http404
    return render(request, 'blog_post.html', {'post': post, 'tags':tags})


def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id, author=request.user)
    form = PostForm(instance=post)
    # import pdb; pdb.set_trace()
    if request.method == "POST":
        form = PostForm(instance=post,data=request.POST)
        if form.is_valid():
            # post.tag.set = request.POST['tag']
            post.date_added = timezone.now()
            post.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            form = PostForm(request.POST)

    context = {'form': form,'post':post}
    return render(request, 'edit_post.html', context)


class ArchiveListView(TemplateView):
    """ Display list of archive list
    """
    template_name = 'archive_list.html'

    def get(self, *args, **kwargs):
        archive = Post.objects.filter(is_archived=True)
        return render(self.request, self.template_name, {'archive': archive})


def archived_post(request, post_id):
    try:
        posts = Post.objects.get(pk=post_id, author=request.user)
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

