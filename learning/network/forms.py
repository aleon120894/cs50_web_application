from django import forms


class RegistrationForm(forms.Form):

    username_field = forms.CharField()
    password_field = forms.CharField()

class PostForm(forms.Form):
    pass