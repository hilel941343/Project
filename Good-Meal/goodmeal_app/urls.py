from django.urls import path
from goodmeal_app import views
from django.contrib.auth import views as auth_views
from .views import recipe_list

urlpatterns = [
    path('',views.goodmeal, name='goodmeal'),
    path('register/', views.register, name='register'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='custom_logout'),
    path('list/',views.recipe_list, name='recipe_list'),
    path('add/', views.add_recipe, name='add_recipe'),
    path('recipes/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),  # Detail view for a specific recipe
    path('recipes/<int:recipe_id>/edit/', views.recipe_edit, name='recipe_edit'),
    path('<int:recipe_id>/delete/', views.recipe_delete, name='recipe_delete'), # Edit view for a specific recipe
]



