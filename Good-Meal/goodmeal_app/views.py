from django.http import HttpResponse
from goodmeal_app.models import Recipe
from goodmeal_app.forms import RecipeForm
from .forms import RegisterForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Recipe
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from .models import RecommendedRestaurant
from .forms import RecommendedRestaurantForm
from django.db.models import Q

# Create your views here.

def index(request):
    context = {
        'index_text': "Welcome to Index page",
    }
    return render(request, 'index.html',context)

def goodmeal(request):
   context = {
        'goodmeal_text': "Welcome to GoodMeal Site"
        
    }
   return render(request, 'goodmeal.html',context)
   
def list_recipe(request):
   context = {
        'goodmeal_text': "Welcome to GoodMeal Site"
        
    }
   return render(request, 'list_recipe.html',context)

def contact(request):
    context = {
        'contact_text': "Welcome to Register"
        
    }
    return render(request, 'contact.html',context)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Redirect to a 'home' page after registration
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Redirect to a 'home' page after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def custom_logout(request):
    print("custom_logout")
    print(request)
    if request.method == 'GET':
        logout(request)
        return redirect('index')  # Redirect to a 'home' page after logout
    return redirect('index')  # Fallback if accessed via GET


# views.py
def recipe_list(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "New recipe added!")
            return redirect('recipe_list')
    else:
        form = RecipeForm()

    all_recipes = Recipe.objects.all()
    paginator = Paginator(all_recipes, 6)  # Paginate by 5 recipes per page
    page = request.GET.get('pg')
    all_recipes = paginator.get_page(page)

    return render(request, 'recipe_list.html', {'all_recipes': all_recipes, 'form': form})



def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

@login_required
def recipe_edit(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm(instance=recipe)
    
    return render(request, 'recipe_edit.html', {'form': form, 'recipe': recipe})

@login_required
def recipe_delete(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, created_by=request.user)  # Ensure the user is the creator
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipe_list')  # Replace with your desired redirect URL

    return render(request, 'recipe_delete.html', {'recipe': recipe})


@login_required(login_url='login')
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')  # Redirect to the recipe list page after saving
    else:
        form = RecipeForm()
    
    return render(request, 'add_recipe.html', {'form': form})

def recommended_restaurant_list(request):
    if request.method == 'POST':
        form = RecommendedRestaurantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recommended_restaurant_list')
    else:
        form = RecommendedRestaurantForm()

    restaurants = RecommendedRestaurant.objects.all()  # Get all recommended restaurants
    return render(request, 'recommended_restaurant_list.html', {'form': form, 'restaurants': restaurants})

@login_required
def add_recommended_restaurant(request):
    if request.method == 'POST':
        form = RecommendedRestaurantForm(request.POST, request.FILES)
        if form.is_valid():
            restaurant = form.save(commit=False)
            restaurant.created_by = request.user
            restaurant.save()
            return redirect('recommended_restaurant_list')
    else:
        form = RecommendedRestaurantForm()
    return render(request, 'add_recommended_restaurant.html', {'form': form})

@login_required
def edit_recommended_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(RecommendedRestaurant, id=restaurant_id, created_by=request.user)
    if request.method == 'POST':
        form = RecommendedRestaurantForm(request.POST, request.FILES, instance=restaurant)
        if form.is_valid():
            form.save()
            return redirect('recommended_restaurant_list')
    else:
        form = RecommendedRestaurantForm(instance=restaurant)
    return render(request, 'edit_recommended_restaurant.html', {'form': form})

@login_required
def delete_recommended_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(RecommendedRestaurant, id=restaurant_id, created_by=request.user)
    if request.method == 'POST':
        restaurant.delete()
        messages.success(request, "Recommended restaurant deleted successfully!")
        return redirect('recommended_restaurant_list')
    return render(request, 'delete_recommended_restaurant.html', {'restaurant': restaurant})

def videos(request):
    return render(request, 'videos.html')