from django.forms import ModelForm
from django import forms

from main.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ('votos', 'autor')
