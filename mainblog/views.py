from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
    reverse
)


from django.http import HttpResponseRedirect, Http404
from django.views.generic import ListView
from django.utils import timezone

from .models import Post, Category, Tag
from .forms import PostForm
from django.contrib.auth.models import User


def index(request):
    import pdb; pdb.set_trace()
    category = Category.objects.all()
    tags = Tag.objects.all()
    posts = Post.objects.filter(is_archived=False)
    if request.user.is_authenticated:
        posts = posts.filter(author=request.user)

    context = {'posts': posts, 'category': category, 'tags':tags}
    return render(request,'home.html', context)

#TODO
#add login required decorator
def create_post(request):
    form =  PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            form = PostForm(request.POST)

    context = {'form': form}
    return render(request, 'create_post.html', context)


def blog_post(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    return render(request, 'blog_post.html', {'post': post})


def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id, author=request.user)
    form = PostForm(instance=post)
    if request.method == "POST":
        form = PostForm(instance=post,data=request.POST)
        if form.is_valid():
            post.date_added = timezone.now()
            post.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            form = PostForm(request.POST)

    context = {'form': form,'post':post}
    return render(request, 'edit_post.html', context)


def archive_list(request):
    #TODO
    #return list arhive post by user
    pass

def archived_post(request, post_id):
    #use try and catch error
    posts = get_object_or_404(Post, pk=post_id, author=request.user)
    posts.is_archived = True
    posts.save()
    return HttpResponseRedirect(reverse('index'))


def category_page(request, category_id):
    get_category = get_object_or_404(Category, pk=category_id)
    posts = Post.objects.filter(category=get_category.id)
    return render(request, 'category_post.html', {'get_category': get_category,'posts': posts})

