from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.http import HttpResponse
from .models import *
from django.views.generic.edit import CreateView

# Create your views here.
def IndexView(request):
    return render(request,'productApp/index.html')

def Home(request):
    return render(request,'productApp/index.html')

def ShopView(request):
    products = Product.objects.all()
    return render(request,'productApp/shop.html',{'products' : products})

def ShopSingleView(request,id):
    obj=get_object_or_404(Product,pk=id)
    return render(request,'productApp/shop-single.html',{'obj':obj})


class DemoCreateView(CreateView):
    model  = Demo
    fields = ['username','profile_pic']
    template_name = "productApp/demo.html"
    success_url = "/"