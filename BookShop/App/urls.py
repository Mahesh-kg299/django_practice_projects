from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index.as_view()),
    path('add/', views.AddBook.as_view()),
    path('show/', views.ShowBook.as_view()),
    path('edit/<name>/', views.EditBook.as_view()),
    path('register/', views.Register.as_view()),
    path('login/', views.Login.as_view()),
    path('logout/', views.Logout.as_view()),
]