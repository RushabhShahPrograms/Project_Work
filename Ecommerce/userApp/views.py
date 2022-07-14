from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.conf import settings
from django.core.mail import send_mail
from .forms import UserForm

# For Email
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import User
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
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

        return redirect('/')
    
def profile(request):
    return render(request, "userApp/profile.html")

def sendMail(request):
    subject = "Test"
    message = "Hello This is Ecommerce"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['01@gmail.com']
    send_mail(subject,message,email_from,recipient_list)
    return HttpResponse("Sent Mail")

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Huff ,Username already exist')
            return redirect("register")
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Come On, Email was already Taken !')
            return redirect("register")
        else:
            user = User.objects.create_user(
                username=username, password=password, email=email)
            mydict = {'username': username}
            user.save()
            html_template = 'userApp/register_email.html'
            html_message = render_to_string(html_template, context=mydict)
            subject = 'Welcome to Service-Verse'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            message = EmailMessage(subject, html_message,
                                   email_from, recipient_list)
            message.content_subtype = 'html'
            message.send()
            return redirect("success")
    else:
        return render(request, 'userApp/register.html')
    
def success(request):
    return render(request,'userApp/success.html')