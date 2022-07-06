from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic.edit import CreateView

# Create your views here.
def IndexView(request):
    return render(request,'productApp/index.html')

def ShopView(request):
    return render(request,'productApp/shop.html')

def ShopSingleView(request):
    return render(request,'productApp/shop-single.html')


class DemoCreateView(CreateView):
    model  = Demo
    fields = ['username','profile_pic']
    template_name = "productApp/demo.html"
    success_url = "/"