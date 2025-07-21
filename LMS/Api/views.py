from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.generics import ListCreateAPIView
from .serializers import BookListSerializer, MemberSerializer
from .models import Book, Member
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT


class BookListCreateAPIView(APIView):
    def get(self, request, farmat = None):
        books = Book.objects.values("title", "author")
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)
        
    def post(self, request: Request, format = None):
        data = request.data.copy()
        last_book = Book.objects.all().order_by('book_id').last()

        if last_book:
            book_id = f'book{int(last_book.book_id.replace("book", "")) + 1:03d}'
        else:
            book_id = 'book001'
        data['book_id'] = book_id
        serializer = BookListSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class BookGetUpdateApiView(APIView):
    def get(self, request, book_id, format=None):
        book = Book.objects.get(book_id=book_id)
        serializer = BookListSerializer(book)
        return Response(serializer.data)
    
    def put(self, request, book_id, format=None):
        book = Book.objects.get(book_id = book_id)
        serializer = BookListSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request, book_id, format=None):
        book = Book.objects.get(book_id=book_id)
        book.delete()
        return Response(status=HTTP_204_NO_CONTENT)
            

class BookListView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    

class MemberListAPIView(APIView):
    def get(self, request, format=None):
        members = Member.objects.all()
        serializer = MemberSerializer(members)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        data = request.data.copy()
        last_member = Member.objects.all().order_by('member_id').last()

        if last_member:
            new_id = f'member{int(last_member.member_id.replace("member", "")) + 1:03d}'
        else:
            new_id = f'member001'

        data['member_id'] = new_id
        serializer = MemberSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, satus=HTTP_400_BAD_REQUEST)