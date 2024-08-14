from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Recipe
from crispy_forms.layout import Submit
from goodmeal_app.models import Recipe
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from .models import RecommendedRestaurant

class RecommendedRestaurantForm(forms.ModelForm):
    class Meta:
        model = RecommendedRestaurant
        fields = ['name', 'photo', 'description','restaurent_url']
       

class RecipeListHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'GET'  # Important for GET requests
        self.layout = Layout(
            Submit('edit', 'Edit', css_class='btn btn-primary'),
            Submit('delete', 'Delete', css_class='btn btn-danger'),
        )

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

    class Meta:
        model = Recipe
        fields = ['recipe', 'composites', 'instructions']

