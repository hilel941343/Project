from django.http import HttpResponse
from goodmeal_app.models import Recipe
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Recipe
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required
from django.conf import settings

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

@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RecipeForm()
    context = {
        'form': form,
        'welcome_message': "Welcome to Share a Recipe"
    }
    return render(request, 'add_recipe.html', context)

def about(request):
    context = {'about_text': "Welcome to Good Meal! Here you can find and share delicious recipes."}
    return render(request, 'about.html', context)