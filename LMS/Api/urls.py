from django.urls import path
from .views import BookListCreateAPIView, BookGetUpdateApiView, MemberListAPIView

urlpatterns = [
    path('books/', BookListCreateAPIView.as_view()),
    path('book/<slug:book_id>', BookGetUpdateApiView.as_view()),
    path('members/', MemberListAPIView.as_view())
]