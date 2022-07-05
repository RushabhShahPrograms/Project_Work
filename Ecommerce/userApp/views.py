from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login, logout

from .forms import UserForm

# Create your views here.
class BaseRegisterView(FormView):

    form_class = UserForm
    template_name ="userApp/register.html"
    success_url = "/"
    
    def form_valid(self, form):
        user = form.save()
        user.set_password = form.cleaned_data['password']
        user.save()
        return super().form_valid(form)

class UserLoginView(LoginView):
    template_name = "userApp/login.html"
    success_url ="/"

def UserLogout(request):
    if request.method == "POST":
        logout(request)

        return redirect('home')
    
def profile(request):
    return render(request, "userApp/profile.html")