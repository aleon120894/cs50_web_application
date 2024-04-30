from django import forms
from .models import Post


class RegistrationForm(forms.Form):

    username_field = forms.CharField()
    password_field = forms.CharField()

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content']
