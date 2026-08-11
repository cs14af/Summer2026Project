from django import forms
from django.contrib.auth.models import User

from .models import Profile

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User

        fields = [
            "first_name",
            "last_name",

        ]

        widgets ={
            "first_name": forms.TextInput(
                attrs={
                    "class ": "form-control",
                    "placeholder" : "Enter your first name",
                }
            ),
            "last_name" : forms.TextInput(
                attrs={
                    "class":"form-control",
                    "placeholder": "Enter your last name",
                }
            ),
        }
