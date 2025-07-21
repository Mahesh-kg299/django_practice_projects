from django.urls import path
from . import views
from rest_framework.authtoken import views as authtoken_view

urlpatterns = [
    path('videos/', views.VideoListView.as_view()),
    path('videos/<pk>/', views.VideoDetailView.as_view()),
    path('users/', views.VTubeUserListView.as_view()),
    path('users/<pk>/', views.VTubeUserDetailView.as_view()),
    path('comments/', views.CommentListView.as_view()),
    path('comments/<pk>/', views.CommentDetailView.as_view()),
    path('register/', views.RegisterUserView.as_view()),
    path('authtoken/', authtoken_view.obtain_auth_token),
]