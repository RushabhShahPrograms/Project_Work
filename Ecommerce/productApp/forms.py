from django import forms
from .models import *

class ProductForm(forms.ModelForm):

    class Meta:
        model = 'Product'
        fields = '__all__'
