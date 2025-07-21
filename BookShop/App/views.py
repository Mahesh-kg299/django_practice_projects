from django.views import View
from django.views.generic import ListView
from . import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Book
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class Index(View):
    def get(self, request):
        return render(request, "App/index.html")

class Register(View):
    def get(self, request):
        form = forms.UserForm()
        return render(request, "App/register.html", {"form": form})

    def post(self, request):
        form = forms.UserForm(request.POST)
        if form.is_valid():

            if User.objects.filter(username = form.cleaned_data["username"]).exists():
                return HttpResponse("User with this username already exist.")

            if form.cleaned_data["password"] != form.cleaned_data["c_password"]:
                return HttpResponse("Password and confirtm password doesn't match.")
            
            user = form.save(commit = False)
            user.set_password(form.cleaned_data["password"])
            form.save()
            return redirect("/app/login/")
        return HttpResponse("There's some error in form.")

class Login(View):
    def get(self, request):
        return render(request, "App/login.html")

    def post(self, request):
        username = request.POST["username"] 
        password = request.POST["password"]

        if not User.objects.filter(username=username).exists():
            return HttpResponse("User with this username doesn't exist.")

        user = authenticate(request, username=username, password = password)

        if not user:
            return HttpResponse("Wrong password!")
        
        login(request, user)

        return redirect("/app/")

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("/app/")

class AddBook(LoginRequiredMixin, View):
    login_url = "/app/login/"

    def get(self, request):
        fm = forms.AddBookForm()
        return render(request, "App/addBook.html", {"form": fm})
    
    def post(self, request):
        form = forms.AddBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/app/show/')
        return HttpResponse("Form has some error.")

class EditBook(View):
    def get(self, request, name):
        book = Book.objects.get(name = name)
        fm = forms.AddBookForm(instance= book)
        return render(request, "App/editBook.html", {"form": fm, "book":book})
    
    def post(self, request, name):
        book = Book.objects.get(name = name)
        form = forms.AddBookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('/app/show/')
        return HttpResponse("From isn't currest.")

class ShowBook(ListView):
    model = Book
    template_name = "App/show.html"
    context_object_name = "books"