from django import forms
from django.core.exceptions import ValidationError

class SignUpForm(forms.Form):
    firstName = forms.CharField(max_length=50)
    lastName = forms.CharField(max_length=50)
    email =  forms.EmailField()
    password = forms.CharField()
    # confirm_password =  forms.CharField()
