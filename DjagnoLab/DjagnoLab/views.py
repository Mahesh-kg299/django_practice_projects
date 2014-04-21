from django.views import View
from django.http import HttpRequest, HttpResponse

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