from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
    reverse
)
from django.http import HttpResponseRedirect, Http404
from django.views.generic import ListView

from .models import Post
from .forms import PostForm
from django.contrib.auth.models import User


def index(request):
    posts = Post.objects.all()
    if request.user.is_authenticated:
        posts = posts.filter(author=request.user)
    context = {'posts': posts}
    return render(request,'home.html', context)


def create_post(request):

    form =  PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return render(request, 'home.html')
        else:
            #print ('Invalid>>>>>>>>>>>>>>>>>>>>>>>>>')
            form = PostForm(request.POST)

    context = {'form': form}
    return render(request, 'create_post.html', context)

def blog_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    """try:
        post = Post.objects.get(id=post_id)
        return render(request, 'blog_post.html', {'post': post})
    except Post.DoesNotExist:
        raise Http404("Post does not exist")"""

    return render(request, 'blog_post.html', {'post': post})

def home(request):
    render(request, 'home.html')

