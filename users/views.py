from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate,logout
from .forms import SignUpForm, LoginForm
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView, View


class SignUpView(TemplateView):
    """ User SignUp View """
    template_name = 'signup.html'

    def get(self, *args, **kwargs):
        form = SignUpForm()
        context = {'form': form}
        return render(self.request, self.template_name, context)

    def post(self, *args, **kwargs):
        form = SignUpForm(self.request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        context = {'form':form }
        return render(self.request, self.template_name, context)


class SignInView(TemplateView):
    """ User SignIn View"""
    template_name = 'login.html'

    def get(self, *args, **kwargs):
        form = LoginForm()
        context = {'form': form}
        return render(self.request, self.template_name, context)

    def post(self, *args, **kwargs):
        form = LoginForm(self.request.POST)

        if form.is_valid():
            user = form.user_cache
            login(self.request, user)
            return HttpResponseRedirect(reverse('index'))
        context = {'form': form}
        return render(self.request, self.template_name, context)


class SignOutView(TemplateView):
    """User SignOut View"""
    template_name = 'logout.html'

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            logout(self.request)
            return render(self.request, self.template_name)


# def signup(request):

#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request,user)
#             return render(request, 'home.html')
#         else:
#             return render(request, 'signup.html', {'form':form, 'error':form.errors})

#     form = SignUpForm()
#     return render(request, 'signup.html', {'form':form})


# def signin(request):
#     form = LoginForm(request.POST)

#     if form.is_valid():
#         user = form.user_cache
#         login(request,user)
#         return HttpResponseRedirect(reverse('home'))
#     else:
#         form = LoginForm(request.POST)
#     return render(request, 'login.html', {'form':form})

# def signout(request):
#     if request.user.is_authenticated:
#         logout(request)
#         return render(request, 'logout.html')

