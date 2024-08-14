from django.db import models
from django.db.models import TextField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from django.contrib.auth.models import User

class StrippingTextField(TextField):
    def formfield(self, **kwargs):
        kwargs['strip'] = True
        return super(StrippingTextField, self).formfield(**kwargs)

class Recipe(models.Model):
    recipe = models.CharField(max_length=30, null=True, blank=True)
    composites = StrippingTextField()  # Keep as TextField for now, consider JSONField later
    instructions = StrippingTextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes', default=1)  # Link to the user who created the recipe

class RecommendedRestaurant(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='restaurant_photos/', blank=True, null=True)
    description = models.TextField()
    restaurent_url=models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name