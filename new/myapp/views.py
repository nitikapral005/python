
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from  django.contrib.auth import login, logout,authenticate
from  django.contrib.auth.forms import UserCreationForm
# Create your views here.
# def index(request):
#     return render(request, "index.html",{})

# def nextt(request):
#     # insert and reterive operations
#    stu = student.objects.all()
#     if request.method=="POST":
#         usr = request.POST.get("Username")
#         eml = request.POST.get("email")
#         ps = request.POST.get("pwd")
#         user = student( username = usr, email= eml, password= ps)
#         user.save()
#     return render(request, "next.html",{'st':stu})

# def updateUser(request , id):
#     st= student.objects.get(pk = id)
#     if request.method=="POST":
#         usr1 = request.POST.get("Username")
#         eml1 = request.POST.get("email")
#         ps1 = request.POST.get("pwd")
#         st.username =usr1
#         st.email =eml1
#         st.password =ps1
#         st.save()
#         return  redirect("nextt")
#     return render(request,'update.html',{'st':st})


#     st= student.objects.get(pk = id)
#     st.delete()
#     return  redirect("nextt")
def index(request):
    frm = StudentForm()
    stu = student.objects.all()
    if request.method == 'POST':
        frm = StudentForm(request.POST , request.FILES)
        if frm. is_valid():
            frm.save()
          # us = frm.cleaned_data["username"]
          # em = frm.cleaned_data["email"]
          # ps = frm.cleaned_data["password"]
        #   imz = frm.cleaned_data["image"]
          # user = student(username=us, email=em, password=ps , image = imz)
          # user.save()
    return render(request, "index.html", {'fr': frm, 'st': stu})


def updateuser(request, id):
    s = student.objects.get(pk=id)
    fr = StudentForm(instance=s)
    if request.method == 'POST':
        fr = StudentForm(instance=s)
        if fr.is_valid():
            fr.save()
            return redirect('/')
    return render(request, "update1.html", {'fr': fr})


def deleteuser(request, id):
    if request.method == "POST":
        s = student.objects.get(pk=id)
        s.delete()
    return redirect("/")

def registeruser(request):
    fr = UserCreationForm()
    if request.method == 'POST':
        fr = UserCreationForm(request.POST)
        if fr.is_valid():
            fr.save()
        return redirect("login")
    return render(request, 'register.html',{'fr': fr})

def loginuser(request):
    if request.method == 'POST':
        usr= request.POST.get('username')
        ps= request.POST.get('pwd')
        user= authenticate(request,username=usr, password=ps)
        if user is not None:
            login(request,user)
        return redirect('/')
    
    return render(request, 'login.html',{})

def logoutuser(request):
    logout(request)
    return redirect("login")
    