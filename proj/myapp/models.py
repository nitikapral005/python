from tkinter import Widget
from django.db import models
from django import forms

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)


Widgets = {
    'name': forms.TextInput(attrs={'class': 'form-control'}),
    'email': forms.EmailInput(attrs={'class': 'form-control'}),
    'password': forms.PasswordInput(attrs={'class': 'form-control'}),
}
