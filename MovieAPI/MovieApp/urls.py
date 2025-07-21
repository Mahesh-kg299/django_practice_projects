from django.urls import path
from . import views
urlpatterns = [
    path("", views.all_add_movies),
    path("<int:mid>/", views.get_movie),
    path("<int:mid>/update/", views.update_movie),
    path("<int:mid>/delete/", views.delete_movie),
]