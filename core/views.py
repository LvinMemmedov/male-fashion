from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from core.models import *
from core.forms import *

from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect


def home(request):
    context={
        'title': 'Hom Page',
        # "setting":Setting.objects.last
        'product':Product.objects.all()
    }
    return render(request, "index.html", context)


def contact(request):
  
    context = {
        'title':"Contact Page",
       
    }
    return render(request,"contact.html",context)


def shop(request):
    context={
       
    }
    return render(request, "shop.html", context)

def about(request):
    context={
       
    }
    return render(request, "about.html", context)

def shop_details(request):
    context={
       
    }
    return render(request, "shop_details.html", context)

def shopping_cart(request):
    context={
       
    }
    return render(request, "shopping_cart.html", context)



def checkout(request):
    context={
       
    }
    return render(request, "checkout.html", context)


def blog_details(request):
    context={

    }
    return render(request,"blog_details.html", context)

def blog (request):
    context={

    }
    return render(request,"blog.html", context)



