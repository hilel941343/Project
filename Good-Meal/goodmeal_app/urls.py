from django.urls import path
from goodmeal_app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.goodmeal, name='goodmeal'),
    path('add/', views.add_recipe, name='add_recipe'),
    path('add/', views.list_recipe, name='list_recipe'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('', views.home, name='home'),
]
