from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    
    path('create/',views.BaseRegisterView.as_view(),name='create'),
    path('login/',views.UserLoginView.as_view(),name='login'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.UserLogoutView,name='logout'),
]
