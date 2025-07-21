from django.urls import path, include
from . import views

urlpatterns = [
    path('states/', views.StateList.as_view()),
    path('states/<int:pk>/', views.StateDetail.as_view()),
    path('chfministers/', views.ChfMinisterList.as_view()),
    path('chfministers/<int:pk>/', views.ChfMinisterDetail.as_view()),
    path('auth/', include('rest_framework.urls')),
]