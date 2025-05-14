from django.contrib import admin
from goodmeal_app.models import Recipe
from goodmeal_app.models import RecommendedRestaurant
# Register your models here.

admin.site.register(Recipe)

admin.site.register(RecommendedRestaurant)
