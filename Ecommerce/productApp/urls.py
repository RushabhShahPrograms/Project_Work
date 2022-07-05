from . import views
from django.urls import path
from .views import *

urlpatterns = [
    
    path('index/',views.IndexView),
    path('demo/',views.DemoCreateView.as_view(),name='demo'),
]