"""
URL configuration for DjagnoLab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import ManageCookieView, ManageSessionView, UserCreateView, UserLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cookies/<str:action>', ManageCookieView.as_view()),
    path('cookies/', ManageCookieView.as_view()),
    path('sessions/<str:action>', ManageSessionView.as_view()),
    path('sessions/', ManageSessionView.as_view()),
    path('create-user/', UserCreateView.as_view()),
    path('login/', UserLoginView.as_view()),
]
