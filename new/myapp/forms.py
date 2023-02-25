from django import forms
from .models import *

from django.contrib.auth.models import User

class StudentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ['username','email','password', 'image']
        widgets ={
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(render_value= True, attrs={'class': 'form-control'}),
                
             }
    
    
class SignupForm(forms.ModelForm):
        class Meta:
            model =  User
            fields=['username', 'first_name','last_name','email','password']  
            widgets ={
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(render_value= True, attrs={'class': 'form-control'}),
        }     