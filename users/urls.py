from django.urls import path
from django.contrib.auth import views as auth_views
from users.views import (
    SignUpView,
    SignInView,
    SignOutView
    )


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', SignInView.as_view(), name='signin'),
    path('logout/', SignOutView.as_view(), name='signout'),

]
