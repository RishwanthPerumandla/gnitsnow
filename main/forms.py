from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Achievement

class DateInput(forms.DateInput):
    input_type = 'date'

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    dob = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}),required=False)

    class Meta:
        model = User
        fields = ["username", "dob","email", "password1", "password2"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description"]

class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievement
        fields = ["title", "description"]