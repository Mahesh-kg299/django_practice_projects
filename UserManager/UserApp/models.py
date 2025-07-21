from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserData(models.Model):
    dob = models.DateField()
    city = models.CharField(max_length=25)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_data')