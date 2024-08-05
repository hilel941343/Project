from django.db import models

class Recipe(models.Model):
    recipe = models.CharField(max_length=200)
    composites = models.TextField(default="")
    instructions = models.TextField(default="")

    def __str__(self):
        return self.recipe
