from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LaptopForm
from .models import Laptop

@login_required(login_url='/auth/signin/')
def add(request):
    if request.method=='POST':
        form=LaptopForm(request.POST)
        if form.is_valid():
            form.save()
            #return HttpResponse("Laptop Added Succussfully. ")
            return redirect('/seller/show/')
    template_name='add.html'
    form=LaptopForm()
    context={'form':form}
    return render(request,template_name,context)

@login_required(login_url='/auth/signin/')
def show(request):
    template_name='show.html'
    objs=Laptop.objects.all()
    context={'objs':objs}
    return render(request, template_name, context)

def update(request,j):
    obj=Laptop.objects.get(id=j)
    if request.method=='POST':
        form=LaptopForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/seller/show/')
    template_name='add.html'
    form=LaptopForm(instance=obj)
    context={'form':form}
    return render(request, template_name, context)

def delete(request,k):
    obj=Laptop.objects.get(id=k)
    if request.method=='POST':
        obj.delete()
        return redirect('/seller/show/')
    template_name = 'delete_confirmation.html'
    context = {'obj':obj}
    return render(request, template_name, context)
