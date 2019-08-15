from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('equipodocente/', views.equipodocente, name= 'equipodocente'),
    path('pestañalibre/', views.pestañalibre, name= 'pestañalibre'),
]
