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


# Create your views here.
def index(request):
    context = {
        'index_text': "Welcome to Index page"
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
            return redirect('home')  # Redirect to a 'home' page after registration
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to a 'home' page after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def custom_logout(request):
    print("custom_logout")
    print(request)
    if request.method == 'GET':
        logout(request)
        return redirect('home')  # Redirect to a 'home' page after logout
    return redirect('home')  # Fallback if accessed via GET

def fetch_random_recipes():
    api_key = settings.SPOONACULAR_API_KEY
    url = f'https://api.spoonacular.com/recipes/random?number=5&apiKey={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('recipes', [])
    return []

def home(request):
    # Fetch random recipes from the API
    random_recipes = fetch_random_recipes()
    
    # Fetch user-added recipes from the database
    user_recipes = Recipe.objects.all()

    return render(request, 'home.html', {
        'random_recipes': random_recipes,
        'user_recipes': user_recipes
    })
# views.py
def recipe_list(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "New recipe added!")
            return redirect('recipe_list')  # Redirect to refresh the page and show the new recipe
    else:
        form = RecipeForm()

    all_recipes = Recipe.objects.all()
    paginator = Paginator(all_recipes, 5)
    page = request.GET.get('pg')
    all_recipes = paginator.get_page(page)
    
    return render(request, 'recipe_list.html', {'all_recipes': all_recipes, 'form': form})

def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe.delete()
    messages.success(request, "Recipe deleted!")
    return redirect('recipe_list')

def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            messages.success(request, "Recipe edited!")
            return redirect('recipe_list')
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'edit.html', {'form': form})

def add_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Recipe added!")
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'add_recipe.html', {'form': form})
