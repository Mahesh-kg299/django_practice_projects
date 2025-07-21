from django.db import models

# Create your models here.
class Industry(models.Model):
    ind_id = models.AutoField(primary_key= True)
    ind_name = models.CharField(max_length= 20)

class Company(models.Model):
    c_id = models.AutoField(primary_key= True)
    c_name = models.CharField(max_length= 35)
    c_founded = models.DateField()
    c_industry = models.ManyToManyField(Industry, related_name='companies')