from . import views
from django.urls import path
from .views import *

urlpatterns = [
    
    path('',views.IndexView,name='index'),
    path('shop/',views.ShopView,name='shop'),
    path('shop-single/',views.ShopSingleView,name='shop-single'),
    path('demo/',views.DemoCreateView.as_view(),name='demo'),
]