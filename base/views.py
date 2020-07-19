from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Datas
from accounts.views import *
#from guardian.core import ObjectPermissionChecker
#from guardian.shortcuts import get_perms
# Create your views here.
def home(request):
    
    data = Datas.objects.all()
    
    return render(request,'home.html',{'data':data})

def add(request):
    if request.method=='POST':
            
        name=request.POST["name"]
        img=request.FILES["img"]
        pdf=request.FILES["pdf"]
        desc=request.POST["desc"]
        add_data = Datas(name=name,img=img,pdf=pdf,desc=desc)
        add_data.save()
        return redirect('add')
    else: 
        
        username = None
        if request.user.is_authenticated:
            username = request.user.username
        the_user = User.objects.get(username=username)
        if the_user.has_perm('base.add_datas'):
            return render(request,'add.html')
        else:
            return redirect('/')