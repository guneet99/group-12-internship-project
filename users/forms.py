from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .models import Activity_Choice,Gender
# from .models import UserRegis

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    first_name=forms.CharField()
    last_name=forms.CharField()
    gender=forms.Select(choices=Gender)
    contact=forms.CharField()
    age=forms.CharField()
    height=forms.CharField()
    weight=forms.CharField()
    activity=forms.Select(choices=Activity_Choice)

    
    class Meta:
        model = Profile
        fields = ['image','first_name','last_name','gender','contact','age','height','weight','activity']