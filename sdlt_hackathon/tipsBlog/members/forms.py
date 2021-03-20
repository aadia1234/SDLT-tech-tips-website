from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .models import *
from django import forms
from django.db import models
from django.contrib.auth.models import User

class RegisterEditorForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'is_staff', 'password1', 'password2')
        


    def __init__(self, *args, **kwargs):
        super(RegisterEditorForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['class'] = 'form-control'