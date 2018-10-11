from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
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
            login(request)
            return render(request, 'home.html')
        else:
            return render(request, 'signup.html', {'form':form, 'error':form.errors})

    form = SignUpForm()
    return render(request, 'signup.html', {'form':form})


def login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(username=username, password=password)
        login(request)
        print (request.user.is_authenticate)
        if request.user.is_authenticated:
            return render(request, 'home.html')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

