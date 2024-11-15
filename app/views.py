from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def Indexpage(request):
    if request.method=='POST':
        uname=request.POST.get('txt')
        mail=request.POST.get('email')
        password=request.POST.get('pswd')
        my_user=User.objects.create_user(uname,mail,password)
        my_user.save()
        return redirect('login')
    return render(request, 'index.html')
def Loginpage(request):
    if request.method=='POST':
        uname=request.POST.get('namee')
        password=request.POST.get('pswd')
        my_user1=authenticate(request,username=uname,password=password)
        if my_user1 is not None:
            login(request,my_user1)
            return redirect('home')
        else:
            return HttpResponse("invalid entry")
    return render(request,'login.html')
@login_required(login_url='login')
def Homepage(request):
    return render(request,'home.html')
def Logoutpage(request):
    logout(request)
    return redirect('login')