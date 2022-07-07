from . import views
from django.urls import path
from .views import *

urlpatterns = [
    
    path('',views.IndexView,name='index'),
    path('index/',views.Home,name='home'),
    path('shop/',views.ShopView,name='shop'),
    path('<int:id>',views.ShopSingleView,name='shop-single'),
    path('demo/',views.DemoCreateView.as_view(),name='demo'),
]