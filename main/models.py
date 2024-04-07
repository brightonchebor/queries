from django.db import models

# Create your models here
class Student(models.Model):
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.firstname
    
class Teacher(models.Model):
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.firstname