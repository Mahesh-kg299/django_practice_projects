from django.db import models

# Create your models here.

class Member(models.Model):
    member_id = models.CharField(primary_key=True, max_length=10)
    name = models.TextField(max_length=25)
    dob = models.DateField()

class Book(models.Model):
    book_id = models.CharField(primary_key=True, max_length=25)
    title = models.TextField(max_length=50)
    author = models.TextField(max_length=25)
    isbn = models.IntegerField(default=0)
    is_borrowed = models.BooleanField(default=False)
    borrowed_by = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='books', null=True)