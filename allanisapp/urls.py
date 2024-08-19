from django.shortcuts import redirect
from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='index'),
    path('register/', views.signup, name='signup'),
]