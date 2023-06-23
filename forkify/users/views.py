from typing import Any, Set
from django.forms.models import BaseModelForm
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from users.models import Users
from users.forms import UsersModelForm,CustomUserCreationForm,CustomUserChangeForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.forms import UserChangeForm



# Create your views here.

class Index(TemplateView):
    template_name = 'users/index.html'
    

class HomePage(TemplateView):
     template_name = "users/homepage.html"


class Registration(CreateView):
    template_name = "users/register.html"
    form_class = CustomUserCreationForm
    queryset = Users.objects.all()
    success_url = reverse_lazy('index')

    # def get_success_url(self) -> str:
    #     return reverse('index')
    
    def form_valid(self, form):
        return super().form_valid(form)
    
    
    
    
class MyLogin(LoginView):
        
        template_name ="users/login.html"  
        authentication_form =LoginForm  

        def get_success_url(self) -> str:
             return reverse('homepage')
        
        
class MyLogout(LogoutView):
     template_name = "users/index.html"
     
     
class UpdateProfile(CreateView):
     template_name ="users/update-profile.html"
     form_class = CustomUserChangeForm
     success_url = reverse_lazy('homepage')     
     
    
    

    
    
   
    
   
    
