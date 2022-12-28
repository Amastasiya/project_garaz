from django.db import models

# Create your models here.

class Employee(models.Model):
    position = models.CharField(default='', max_length=1024)
    surname = models.CharField(default='', max_length=1024)
    name = models.CharField(default='', max_length=1024)
    fathername = models.CharField(default='', max_length=1024)
    birthdate = models.DateField()
    phone_working = models.IntegerField()
    phone_personal = models.IntegerField()
    email_working = models.CharField(default='', max_length=1024)

class Guide(models.Model):
    position = models.CharField(default='', max_length=1024)
    surname = models.CharField(default='', max_length=1024)
    name = models.CharField(default='', max_length=1024)
    fathername = models.CharField(default='', max_length=1024)
    birth_date = models.DateField()
    phone_working = models.IntegerField()
    phone_personal = models.IntegerField()
    email_working = models.CharField(default='', max_length=1024)

