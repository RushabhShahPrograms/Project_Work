from . import views
from django.urls import path
from .views import *

urlpatterns = [
    
    path('',IndexView.as_view(),name='index'),
    path('about/',About.as_view(),name='about'),
    path('contact/',Contact.as_view(),name='contact'),
    path('shop/',views.ShopView,name='shop'),
    path('shopsingle/<pk>',views.ShopSingleView,name='shop-single'),
    path('demo/',views.DemoCreateView.as_view(),name='demo'),
    path('addtocart/<pk>',views.add_to_cart,name='add_to_cart'),
]