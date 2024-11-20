from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect


def signUp(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #return HttpResponse('User Added')
            return redirect('/auth/signin/')
    template_name='signup.html'
    form=UserCreationForm()
    context={'form':form}
    return render(request, template_name, context)

def signIn(request):
    if request.method=='POST':
        u=request.POST['uname']
        p=request.POST['pw']
        print("User name : ",u,"Password : ",p)
        user=authenticate(username=u,password=p)
        if user is not None:
            login(request,user)
            return redirect('/seller/show/')
    template_name='signin.html'
    context={}
    return render(request, template_name, context)

def logoutView(request):
    logout(request)
    return redirect('/auth/signin/')
