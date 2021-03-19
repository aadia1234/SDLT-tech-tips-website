from django import forms
from tinymce.widgets import TinyMCE
from .models import Post, Category

choices = Category.objects.all().values_list('name', 'name')

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = '__all__'

    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control'}),
      'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
      'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user', 'type': 'hidden'}),
      # 'author': forms.Select(attrs={'class': 'form-control'}),
      'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
      'snippet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'this is a short, brief summary of the post'}),
      'body': TinyMCE(attrs={'required': False, 'cols': 30, 'rows': 20}),
    }

class EditForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title', 'title_tag', 'snippet', 'body')

    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control'}),
      'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
      'snippet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'this is a short, brief summary of the post'}),
      'body': TinyMCE(attrs={'required': False, 'cols': 30, 'rows': 20}),
    }