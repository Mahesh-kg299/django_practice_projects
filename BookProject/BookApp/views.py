from django.http import HttpRequest, JsonResponse
from .models import Book

def index(request):
    book_num = Book.objects.count()
    if book_num:
        result = Book.objects.all()
        books = []
        for book in result:
            books.append({
                "book": {
                    "id": book.b_id,
                    "title": book.title,
                    "author": book.author,
                    "price": book.price,
                }
            })
        return JsonResponse({
            "status": "successfull",
            "data": {
                "number_of_books": book_num,
                "books": books
            }
        })
    return JsonResponse({
        "status": "successfull",
        "data": {
            "number_of_books": book_num,
        }
    }) 


def get_book(request, bid):
    try:
        result = Book.objects.get(b_id = bid)
        book = {
            "id": result.b_id,
            "title": result.title,
            "author": result.author,
            "price": result.price,
        }
        return JsonResponse({
            "status":"Book found.",
            "data":{
                "book": book
            }
        })
    except Book.DoesNotExist:
        return JsonResponse({
            "status": "Book with this id not found."
        })

def add_book(request: HttpRequest):
    book = Book(
        title = request.GET.get("title"),
        author = request.GET.get("author"),
        price = request.GET.get("price"),
    )
    book.save()
    return JsonResponse({
        "status": "Book is added successfully"
        })

def update_book(request: HttpRequest, bid):
    try:
        result = Book.objects.get(b_id = bid)
        result.title = request.GET.get("title")
        result.author = request.GET.get("author")
        result.price = request.GET.get("price")
        result.save()
        return JsonResponse({
            "status": "Book updated successfully."
        })
    except Book.DoesNotExist:
        return JsonResponse({
            "status": "Book with this id not found."

        })

def delete_book(request, bid):
    try:
        result = Book.objects.get(b_id = bid)
        result.delete()
        return JsonResponse({
            "status": "Book deleted successfully."
        })
    except Book.DoesNotExist:
        return JsonResponse({
            "status": "Book with this id not found."
        })