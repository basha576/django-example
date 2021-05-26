from django import forms
from django.contrib.auth.models import User
from basic_app.models import userinfo
class userform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model= User
        fields={'username','password','email'}

class userinfoform(forms.ModelForm):
    class Meta():
        model=userinfo
        fields="__all__"
