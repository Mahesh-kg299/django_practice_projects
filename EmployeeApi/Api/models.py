from django.db import models

# Create your models here.

class Department(models.Model):
    dprt_id = models.AutoField(primary_key= True)
    dprt_name = models.CharField(max_length= 15)
    def __str__(self):
        return self.dprt_name

class Employee(models.Model):
    e_id = models.AutoField(primary_key= True)
    e_name = models.CharField(max_length= 30)
    e_gender = models.CharField(max_length= 1, choices=[
        ('m', "Male"),
        ('f', "Female"),
        ('o', "Other"),
    ])
    e_dob = models.DateField()
    e_salary = models.IntegerField()
    e_email = models.EmailField()
    e_dprt = models.ForeignKey(Department, related_name="employee", on_delete=models.CASCADE)
    def __str__(self):
        return self.e_name