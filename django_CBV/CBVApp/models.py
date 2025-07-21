from django.db import models

# Create your models here.
class Users(models.Model):
    u_id = models.AutoField(primary_key=True)
    u_name = models.CharField(max_length=25)
    u_city = models.CharField(max_length=30)
    u_gender = models.CharField(max_length=1, choices= [
        ("m", "male"),
        ("f", "female"),
        ("o", "others"),
    ])