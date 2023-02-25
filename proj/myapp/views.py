import re
from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.


def index(request):
    fm = StudentRegistration()
    stu = User.objects.all()
    if request.method == "POST":
        fm = StudentRegistration(request.POST, request.FILES)

        if fm.is_valid():
            fm.save()
    return render(request, 'index.html', {'form': fm, 'st': stu})


def deleteuser(request, id):
    if request.method == "POST":
        s = User.objects.get(pk=id)
        s.delete()
    return redirect("/")


def updateuser(request, id):
    s = User.objects.get(pk=id)
    fr = StudentRegistration(instance=s)
    if request.method == "POST":
        fr = StudentRegistration(instance=s)
        if fr.is_valid():
            fr.save()
        return redirect("/")

    return render(request, 'update.html', {"fr": fr})
