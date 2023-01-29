from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=500)
    address = models.CharField(max_length=1000)
    DOB = models.DateField()
    contact = models.IntegerField()
    
    