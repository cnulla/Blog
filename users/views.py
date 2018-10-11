from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from .forms import SignUpForm, LoginForm
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def signup(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request,user)
            return render(request, 'home.html')
        else:
            return render(request, 'signup.html', {'form':form, 'error':form.errors})

    form = SignUpForm()
    return render(request, 'signup.html', {'form':form})


def signin(request):
    form = LoginForm(request.POST)
   # import pdb;pdb.set_trace()
    if form.is_valid():
        user = form.user_cache
        login(request,user)
        return  redirect('home')
    return render(request, 'login.html', {'form':form})

def signout(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request, 'logout.html')
