from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Achievement


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    firstname = forms.CharField()
    lastname = forms.CharField()
    year = forms.CharField()
    branch = forms.CharField()
    section = forms.CharField()
    

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "firstname", "lastname", "year", "branch", "section"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description"]

class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievement
        fields = ["title", "description"]