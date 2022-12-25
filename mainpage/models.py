from django.db import models

# Create your models here.

class Employee(models.Model):
    position = models.CharField(default='', max_length=1024)
    surname = models.CharField(default='', max_length=1024)
    name = models.CharField(default='', max_length=1024)
    fathername = models.CharField(default='', max_length=1024)
    date_of_birth = models.DateTimeField()
    phone = models.IntegerField()
    email = models.CharField(default='', max_length=1024)
