from dataclasses import fields
from django import forms
from . models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=('username', 'email', 'password')

        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control','class':'form-group mb-3'}),
            'password':forms.PasswordInput(attrs={'class':'flow-control','class':'form-group mb-3'}),
        }
