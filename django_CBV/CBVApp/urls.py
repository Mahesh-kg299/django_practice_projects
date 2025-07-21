from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexTemplateView.as_view()),
    path("<pk>/", views.UserDetail.as_view())
]