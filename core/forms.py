from django import forms
from django.http import request
from .models import *
from django.contrib.auth.models import User

class UserForm(forms.Form):	
	username = forms.CharField(min_length=3, max_length=50)
	password = forms.CharField(min_length=8, max_length=20)
	first = forms.CharField(min_length=3, max_length=50)
	last = forms.CharField(min_length=3, max_length=50)
	email = forms.CharField(min_length=3, max_length=50)
