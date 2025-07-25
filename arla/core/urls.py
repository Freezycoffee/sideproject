from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html',authentication_form=LoginForm,), name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.LogoutView, name='logout'),
    path('browse/', views.browse, name='browse'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
]