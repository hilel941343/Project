from django.urls import path
from goodmeal_app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.goodmeal, name='goodmeal'),
    path('register/', views.register, name='register'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('', views.home, name='home'),
    path('',views.recipe_list, name='recipe_list'),
    path('delete/<int:recipe_id>/', views.delete_recipe, name='delete_recipe'),
    path('edit/<int:recipe_id>/', views.edit_recipe, name='edit_recipe'),
    path('add/', views.add_recipe, name='add_recipe'),
]
