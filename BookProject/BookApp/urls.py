from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("add/", views.add_book),
    path("<bid>/", views.get_book),
    path("<bid>/update/", views.update_book),
    path("<bid>/delete/", views.delete_book),
]