from django import forms

class PropertyCreateForm(forms.Form):
    property_name = forms.CharField(label="Property name", max_length=100)

class UserCreateForm(forms.Form):
    username = forms.CharField(label = "Username", max_length=20)
    email = forms.CharField(label = "email", max_length=100)
    password=forms.CharField(widget=forms.PasswordInput, label="Password")

class LoginForm(forms.Form):
    username = forms.CharField(label = "Username", max_length=20)
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

