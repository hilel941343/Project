from django.http import HttpResponse
from goodmeal_app.models import TaskList
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def goodmeal(request):
   context = {
        'goodmeal_text': "Welcome to GoodMeal Site"
        
    }
   return render(request, 'goodmeal.html',context)
   

def contact(request):
    context = {
        'contact_text': "Welcome to Register"
        
    }
    return render(request, 'contact.html',context)

def about(request):
    context = {
        'about_text': "Welcome to Share a Recipe"
        
    }
    return render(request, 'about.html',context)

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
# views.py
from django.shortcuts import render

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
    print(request)
    if request.method == 'GET':
        logout(request)
        return redirect('home')  # Redirect to a 'home' page after logout
    return redirect('home')  # Fallback if accessed via GET
def home(request):
    return render(request, 'home.html')
