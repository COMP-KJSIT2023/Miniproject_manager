from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Registerform(UserCreationForm):
    Group_name = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={'placeholder': 'Enter your Group Number'}))
    Group_member_1 = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'placeholder': 'Group member name'}))
    Group_member_2 = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'placeholder': 'Group member name'}))
    Group_member_3 = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'placeholder': 'Group member name - leave blank if not applicable'}))
    Group_member_4 = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'placeholder': 'Group member name - leave blank if not applicable'}))
    class Meta:
        model = User
        fields = ["username","Group_name","Group_member_1","Group_member_2","Group_member_3","Group_member_4","password1","password2",]
        

class Superform(UserCreationForm):
    first_name = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    year_of_exp = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Years of experience'}))
    specialization = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'placeholder': 'Your specialization (optional)'}))
    class Meta:
        model = User
        fields = ["first_name","last_name","username","password1","password2","year_of_exp","specialization"]
        
class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)