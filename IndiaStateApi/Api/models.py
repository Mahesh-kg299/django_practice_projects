from django.db import models

# Create your models here.

class State(models.Model):
    sid = models.AutoField(primary_key = True)
    name = models.CharField(max_length=20)
    capital = models.CharField(max_length=20)
    population = models.IntegerField()


class ChfMinister(models.Model):
    cmid = models.AutoField(primary_key = True)
    name = models.CharField(max_length=20)
    dob = models.DateField(max_length=20)
    gender = models.CharField(max_length=1)
    state_id = models.OneToOneField(State, on_delete = models.CASCADE, related_name="cm") 