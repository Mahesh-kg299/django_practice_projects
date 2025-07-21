from django.db import models

# Create your models here.
class Genre(models.Model):
    g_id = models.AutoField(primary_key=True)
    g_name = models.CharField(max_length=15)

class Movie(models.Model):
    m_id = models.AutoField(primary_key=True)
    m_title = models.CharField(max_length=50)
    m_box_office = models.BigIntegerField()
    genre = models.ManyToManyField(Genre)