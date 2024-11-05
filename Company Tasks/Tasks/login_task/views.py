from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import login_task
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.

def signuppage(request):
    if request.method =='POST':
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        password = request.POST['pwd']


        user = login_task.objects.filter(email=email)

        if user:
            message = "User already Exist"
            return render (request,"signup.html",{'msg':message})

        empno = login_task(name=name,email=email,number=number,password=password)
        empno.save()

        return redirect('loginurl')
        print(name,email,number,password)

    return render (request,"signup.html")


def loginpage(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = login_task.objects.filter(email=email, password=password).first()
        # user = authenticate(request, username = email, password = password)

        print(request.user)

        if user is not None:
            # empno=login(request,user.username)
            # return redirect('successurl')
            request.session['user_id'] = user.id
            request.session['email'] = user.email
            return redirect('sucessurl')
        else:
            messages.error(request,'Invalid credentials')
            return render (request,'login.html')
    return render (request,'login.html')

def success(request):
    return HttpResponse('login success')
