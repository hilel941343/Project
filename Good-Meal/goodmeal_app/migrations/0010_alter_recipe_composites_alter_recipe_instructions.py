# Generated by Django 5.0.7 on 2024-08-10 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goodmeal_app', '0009_alter_recipe_composites_alter_recipe_instructions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='composites',
            field=models.TextField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='instructions',
            field=models.TextField(),
        ),
    ]