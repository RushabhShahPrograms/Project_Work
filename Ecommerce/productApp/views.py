from pyexpat.errors import messages
import datetime
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render, get_list_or_404
from django.http import HttpResponse
from django.views import View
from .models import *
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    cats = Category.objects.all()
    template_name = "productApp/index.html"

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class Contact(TemplateView):
    template_name = "productApp/contact.html"

class About(TemplateView):
    template_name = "productApp/about.html"

def ShopView(request):
    products = Product.objects.all()
    return render(request,'productApp/shop.html',{'products' : products})

def ShopSingleView(request,pk):
    obj=get_object_or_404(Product,pk=pk)
    return render(request,'productApp/shop-single.html',{'obj':obj})

def add_to_cart(request,pk):
    product = Product.objects.get(pk=pk)

    order_item, created = OrderItem.objects.get_or_create(
        product = product,
        user = request.user,
        ordered = False,
    )

    order_qs = Order.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(product__pk = pk).exists():
            order_item.quantity += 1
            order_item.save()
            return redirect("shop-single",pk=pk)
        else:
            order.items.add(order_item)
            return redirect("shop-single",pk=pk)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user,ordered_date=ordered_date)
        order.items.add(order_item)
        return redirect("shop-single",pk=pk)


class DemoCreateView(CreateView):
    model  = Demo
    fields = ['username','profile_pic']
    template_name = "productApp/demo.html"
    success_url = "/"