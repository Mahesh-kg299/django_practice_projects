from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view()),
    path('register/', views.Register.as_view()),
    path('login/', views.Login.as_view()),
    path('logout/', views.Logout.as_view()),
    path('change_password/', views.ChangePassword.as_view()),
    path('delete/', views.DeleteAcount.as_view()),
    path('forgate_password/', views.ForgatePassword.as_view()),
    path('profile/', views.Profile.as_view()),
]