from django import forms
from .models import Book
from django.contrib.auth.models import User

class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["name", "author", "pages", "price", "cover"]
        labels = {
            "name": "Name",
            "pages": "Pages",
            "author": "Author",
            "price": "Price",
            "cover": "Cover image",
        }
        widgets = {
            "name": forms.TextInput(attrs = {"class": "form-control"}),
            "pages": forms.NumberInput(attrs = {"class": "form-control"}),
            "author": forms.TextInput(attrs = {"class": "form-control"}),
            "price": forms.NumberInput(attrs = {"class": "form-control"}),
            "cover": forms.ClearableFileInput(attrs = {"class": "form-control"}),
        }


class UserForm(forms.ModelForm):
    c_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs = {"class": "form-control"}))
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "password"]
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "email": "Email",
            "username": "Username",
            "password": "Password",
        }
        widgets = {
            "first_name": forms.TextInput(attrs = {"class": "form-control"}),
            "last_name": forms.TextInput(attrs = {"class": "form-control"}),
            "email": forms.EmailInput(attrs = {"class": "form-control"}),
            "username": forms.TextInput(attrs = {"class": "form-control"}),
            "password": forms.PasswordInput(attrs = {"class": "form-control"}),
        }