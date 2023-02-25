from django import forms
from .models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ['username','email','password']
        widgets ={
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(render_value= True, attrs={'class': 'form-control'}),
        }