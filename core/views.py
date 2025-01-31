from django.shortcuts import render,redirect
from item.models import Category,Item
from .forms import *

def index(request):
    items = Item.objects.filter(is_sold = False)[0:6]
    categories = Category.objects.all()
    return render(request,'index.html',{
                  'items':items,
                  'categories':categories
    })

def contact(request):
    return render(request,'contact.html')

def Signup(request):

    if request.method =='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:login')

    else:
        form = SignupForm()

        
    return render(request,'signup.html',{'form':form})

