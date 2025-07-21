from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .models import UserData

class Home(View):
    def get(self, request):
        return render(request, "UserApp/index.html")

class Register(View):
    def get(self, request):
        return render(request, "UserApp/register.html")
    
    def post(self, request):
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        dob = request.POST["dob"]
        city = request.POST["city"]
        username = request.POST["username"]
        password = request.POST["password"]
        c_password = request.POST["c_password"]

        if User.objects.filter(username=username).exists():
            return render(request, "UserApp/massage.html", {"msg": "User with this username already exist."})
        if password != c_password:
            return render(request, "UserApp/massage.html", {"msg": "Password didn't match"})
        user = User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        user.set_password(password)
        user.save()
        user_data = UserData.objects.create(
            dob=dob,
            city=city,
            user_id = user
        )
        user_data.save()
        return render(request, "UserApp/massage.html", {"msg": "User added successfully."})

class Login(View):
    def get(self, request):
        return render(request, "UserApp/login.html")

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        if not User.objects.filter(username=username).exists():
            return render(request, "UserApp/massage.html", {"msg": "User with this username doesn't exist."})
        
        user = authenticate(request, username = username, password = password)
        if not user:
            return render(request, "UserApp/massage.html", {"msg": "This password is incurrect!"})
        
        login(request, user)

        return redirect("/app/profile/")

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("/app/")

class ChangePassword(View):
    def get(self, request):
        return render(request, "UserApp/changePassword.html")

    def post(self, request):
        if request.user.is_authenticated:
            password = request.POST['password']
            c_password = request.POST['c_password']
            if password != c_password:
                return render(request, "UserApp/massage.html", {"msg": "Password didn't match"})
            user = request.user
            user.set_password(password)
            user.save()
            update_session_auth_hash(request, user)
            return redirect("/app/profile/")

class DeleteAcount(View):
    def get(self, request):
        return render(request, "UserApp/deleteAccount.html")
    
    def post(self, request):
        if request.user.is_authenticated:
            password = request.POST["password"]
            user = request.user
            if not user.check_password(password):
                return render(request, "UserApp/massage.html", {"msg": "Incurrest password!"})
            user.delete()
            logout(request)
            return render(request, "UserApp/massage.html", {"msg": "Your account is deleted successfully."})
                

class ForgatePassword(View):
    def get(self, request):
        return render(request, "UserApp/forgatePassword.html")

    def post(self, request):
        username = request.POST["username"]
        password = request.POST['password']
        c_password = request.POST['c_password']
        if not User.objects.filter(username=username).exists():
            return render(request, "UserApp/massage.html", {"msg": "User with this username doesn't exist."})
        if password != c_password:
            return render(request, "UserApp/massage.html", {"msg": "Password didn't match"})
        user = User.objects.get(username=username)
        user.set_password(password)
        user.save()
        return redirect("/app/login/")


class Profile(View):
    def get(self, request):
        if request.user.is_authenticated:
            user_data = UserData.objects.get(user_id = request.user.id)
            return render(request, "UserApp/profile.html", {"user": request.user, "user_data": user_data})
        return redirect("/app/login/")