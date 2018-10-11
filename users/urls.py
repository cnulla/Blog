from django.conf.urls import url
from . import views

urlpatterns = [
    url('signup/', views.signup, name='signup'),
    url('login/', views.signin, name='signin'),
    url('logout/', views.signout, name='signout'),
]
