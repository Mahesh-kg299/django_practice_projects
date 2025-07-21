from rest_framework import viewsets
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ViewSet):
    def list(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        book = Book.object.get(pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)