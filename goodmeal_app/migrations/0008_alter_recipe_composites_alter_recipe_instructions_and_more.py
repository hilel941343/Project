# Generated by Django 5.0.7 on 2024-08-05 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goodmeal_app', '0007_recipe_composites_recipe_instructions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='composites',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='instructions',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipe',
            field=models.CharField(max_length=100),
        ),
    ]
