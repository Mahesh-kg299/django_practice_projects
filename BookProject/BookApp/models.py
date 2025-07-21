from django.db import models

class Book(models.Model):
    b_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=25)
    price = models.IntegerField()
    
