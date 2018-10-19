from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate,logout
from .forms import SignUpForm, LoginForm
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponseRedirect


def signup(request):
    form = SignUpForm()
    template = 'signup.html'

    if request.method == 'POST':

        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request,user)
            return HttpResponseRedirect(reverse('index'))
    return render(request, template, {'form':form})


def signin(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.user_cache
            login(request,user)
            return HttpResponseRedirect(reverse('index'))
    return render(request, 'login.html', {'form':form})

def signout(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request, 'logout.html')



