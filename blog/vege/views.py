from django.shortcuts import render,redirect
from .models import *
from django.db import connection
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'home.html')
@login_required(login_url="/login/")
def receipes(request):
    if request.method=="POST":
        data = request.POST
        rec_name = data.get('rec_name')
        rec_desc = data.get('rec_desc')
        rec_img = request.FILES.get('rec_img')


        Receipe.objects.create(
            rec_name=rec_name,
            rec_desc=rec_desc,
            rec_img=rec_img,
        )
        return redirect('/receipe')
        
    queryset= Receipe.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(rec_name__icontains = request.GET.get('search'))
    context={'receipes': queryset}   
    return render(request,'receipe.html',context)

@login_required(login_url="/login/")
def deletereceipe(request,id):
    queryset= Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/receipe/')
    
@login_required(login_url="/login/")
def updatereceipe(request,id):
    queryset = Receipe.objects.get(id=id)
    if request.method=="POST":
        data = request.POST
        rec_name = data.get('rec_name')
        rec_desc = data.get('rec_desc')
        rec_img = request.FILES.get('rec_img')
        
        queryset.rec_name=rec_name
        queryset.rec_desc=rec_desc
        if rec_img:
            queryset.rec_img=rec_img

        queryset.save()
        return redirect('/receipe')
    context={'receipe': queryset}   
    return render(request,'update_receipe.html',context)


def login_page(request):
    if request.method=="POST":
        username= request.POST.get('username')
        password= request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request,'Invalid Username')
            return redirect('/login')

        user = authenticate(username= username,password=password)

        if user is None:
            messages.error(request,'Invalid Password')
            return redirect('/login')

        else:
            login(request,user)
            return redirect('/receipe')

    return render(request,'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')


def register(request):
    if request.method=="POST":
        first_name= request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        username= request.POST.get('username')
        password= request.POST.get('password')


        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request,'Username already taken')
            return redirect('/register/')
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username

        )
        user.set_password(password)
        user.save()

        messages.info(request, 'Account created Successfully')
        return redirect('/register/')





    return render(request, 'register.html')