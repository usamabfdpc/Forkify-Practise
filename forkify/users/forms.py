from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm

from .models import Users

class UsersModelForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ["username","email","password","role"]
        

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Users
        fields = UserCreationForm.Meta.fields + ('email','role',)

    def __init__(self,*args,**kwargs) -> None:
        super().__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class']='form-control mt-3'
        self.fields['role'].widget.attrs['class']='form-select form-control mt-3'        
        self.fields['email'].widget.attrs['class']='form-control  mt-3'
        self.fields['password1'].widget.attrs['class']='form-control  mt-3'
        self.fields['password2'].widget.attrs['class']='form-control  mt-3'
            

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Users
        fields =['username','email','image']


class LoginForm(AuthenticationForm):
    # class Meta:
    #     model = "Users"
    #     fields = ('username')

    def __init__(self, request: Any = ..., *args: Any, **kwargs):
        super().__init__(request, *args, **kwargs)        
        self.fields['username'].widget.attrs['class']='form-control mt-3'
        self.fields['password'].widget.attrs['class']='form-control mt-3'   

class ResetForm(PasswordChangeForm):

    def __init__(self, request: Any = ..., *args: Any, **kwargs):
        super().__init__(request, *args, **kwargs)        
        self.fields['email'].widget.attrs['class']='form-control mt-3'
           