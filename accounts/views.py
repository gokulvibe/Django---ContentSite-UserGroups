from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages


csv_filepathname="C:/Users/ACER/KIC/projectone/accounts/Testdata1.csv"
    
your_djangoproject_home="C:/Users/ACER/KIC/"
import sys,os
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] ='sw2.settings'

import csv
# Create your views here.

def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('login')
    else:
        return render(request,'login.html')



def register(request):
    if request.method=='POST':
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        username=request.POST["username"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]
        email=request.POST["email"]
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'E=mail taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print("User Created!")
                return redirect('login')
        else:
            messages.info(request,'Passwords do not match')
            return redirect('register')
        
    else:
        return render(request,'register.html')
    
    
def logout(request):
    auth.logout(request)
    return redirect('/')


def update(request):
    
    f = open("C:\\Users\\ACER\\KIC\\projectone\\accounts\\datas.txt","r")
    lst = []
    for data in f:
        lst.append(data[:-1])
    for i in lst:
        new = i.split(",")
        try:
            user = User.objects.get(email = new[2])
            user.first_name = new[0]
            user.last_name = new[1]
            user.save()
        except:
            print("Error master!")
    return redirect('/')
