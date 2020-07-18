from django import forms
from django.contrib.auth.models import User
from .models import User_info


class user_info_form(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username','email','password')


class profile_info_form(forms.ModelForm):
    class Meta:
        model = User_info
        fields = ('portfolio','profile_pic')
