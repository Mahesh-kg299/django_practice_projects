from django.views import View
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect

class ManageCookieView(View):
    def get(self, request: HttpRequest, action=None):
        if action == 'set':
            username = request.GET.get('username', 'guest')
            respose = HttpResponse('Cookie: username set.')
            respose.set_cookie('username', username, max_age=3600, httponly=True, secure=True)
            return respose
        elif action == 'delete':
            respose = HttpResponse('Cookie: username deleted.')
            respose.delete_cookie('username')
            return respose
        else:
            username = request.COOKIES.get('username')
            if username:
                return HttpResponse(f'Username is: {username}')
            else:
                return HttpResponse('No username is set.')
    
class ManageSessionView(View):
    def get(self, request:HttpRequest, action=None):
        if action == 'set':
            username = request.GET.get('username', 'guest')
            request.session['username'] = username
            return HttpResponse('Session: username set.')
        elif action == 'delete':
            try:
                del request.session['username']
                return HttpResponse('Session: username deleted.')
            except KeyError:
                return HttpResponse('Error: username does not exist.')
        elif action == 'terminate':
            request.session.flush()
            return HttpResponse('Session is terminated.')
        else:
            username = request.session.get('username')
            if username:
                return HttpResponse(f'Username is: {username}')
            else:
                return HttpResponse('No username is set.')
            

class UserCreateView(View):
    def get(self, request):
        context = {
            'username': request.GET.get('username'),
            'password': request.GET.get('password'),
        }
        return render(request, 'user_create_form.html', context)
    

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            return redirect('/create-user')
        if User.objects.filter(username=username).exists():
            return redirect('/create-user')
        User.objects.create_user(username = username, password = password)
        return HttpResponse(f'User created successefully. </br>Username: {username}</br>Password: {password}')
    
class UserLoginView(View):
    def get(self, request):
        return render(request, 'login_form.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            return redirect('/login/')
        user = authenticate(username=username, password=password)
        if user:
            return HttpResponse('Authenticated')
        return HttpResponse('Invalid credentials')