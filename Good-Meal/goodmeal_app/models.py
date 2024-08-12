from django.db import models
from django.db.models import TextField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field

class StrippingTextField(TextField):
    def formfield(self, **kwargs):
        kwargs['strip'] = True
        return super(StrippingTextField, self).formfield(**kwargs)
    
class Recipe(models.Model):
    recipe = models.CharField(max_length=30, null=True, blank=True)
    composites =StrippingTextField() # Keep as TextField for now, consider JSONField later
    instructions = StrippingTextField()

