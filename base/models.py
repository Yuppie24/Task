from django.db import models

# Create your models here.
class Student(models.Model):
    name =models.CharField(max_length=100)
    age= models.IntegerField()
    address=models.CharField(max_length=100)
    grade=models.IntegerField()         #6th Grade student- meaning the level of education
    major=models.CharField(max_length=100)