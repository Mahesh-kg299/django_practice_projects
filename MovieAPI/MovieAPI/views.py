from django.shortcuts import render
from django.http import HttpResponse

def show_api_tester(request):
    # return HttpResponse("ok")
    return render(request, "api_tester.html")