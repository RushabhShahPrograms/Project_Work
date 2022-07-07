from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.conf import settings
from django.core.mail import send_mail

from .forms import UserForm

# Create your views here.
class BaseRegisterView(FormView):

    form_class = UserForm
    template_name ="userApp/register.html"
    success_url = "/user/login"
    
    def form_valid(self, form):
        user = form.save()
        user.is_staff = True
        user.password = make_password(form.cleaned_data['password'])
        user.save()
        return super().form_valid(form)

class UserLoginView(LoginView):
    template_name = "userApp/login.html"
    success_url ="/"

def UserLogoutView(request):
    if request.method == "POST":
        logout(request)

        return redirect('home')
    
def profile(request):
    return render(request, "userApp/profile.html")

def sendMail(request):
    subject = "Test"
    message = "Hello This is Ecommerce"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['rushabhshah122000@gmail.com','techyrushabh@gmail.com','mixedthinkerblog@gmail.com']
    send_mail(subject,message,email_from,recipient_list)
    return HttpResponse("Sent Mail")