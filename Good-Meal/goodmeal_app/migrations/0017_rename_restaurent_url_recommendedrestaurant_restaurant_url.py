# Generated by Django 5.0.7 on 2024-08-26 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodmeal_app', '0016_alter_recipe_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recommendedrestaurant',
            old_name='restaurent_url',
            new_name='restaurant_url',
        ),
    ]