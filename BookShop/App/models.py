from django.db import models

# Create your models here.

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    pages = models.IntegerField()
    author = models.CharField(max_length=25)
    price = models.IntegerField()
    cover = models.ImageField(upload_to="covers/")