from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def IndexView(request):
    return HttpResponse('This is index page')


