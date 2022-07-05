from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic.edit import CreateView

# Create your views here.
def IndexView(request):
    return HttpResponse('This is index page')


class DemoCreateView(CreateView):
    model  = Demo
    fields = ['username','profile_pic']
    template_name = "productApp/demo.html"
    success_url = "/"