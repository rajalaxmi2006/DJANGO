from django.db import models

# Create your models here.
class Student(models.Model) :
    name = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    address = models.TextField()
    dob = models.DateField()