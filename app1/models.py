from django.db import models

# Create your models here.
class Student(models.Model):
    Student_Name=models.CharField(max_length=50)
    Classs=models.IntegerField(max_length=4)
    Mother_Name=models.CharField(max_length=50)
    Contact_No=models.IntegerField(max_length=50)
    Address=models.CharField(max_length=50)    
    Adhar_No=models.IntegerField(max_length=50)


    # Teacher_Name=models.CharField(max_length=50)
    # Salary=models.IntegerField(max_length=50,default=10000)
    # Subject=models.CharField(max_length=30,default='maths')


def __str__(self):
    return self.name

class Teacher(models.Model):
    Teacher_Name=models.CharField(max_length=40)
    Subject=models.CharField(max_length=30)
    Contact_No=models.IntegerField(max_length=10)
    Salary=models.IntegerField(max_length=6)


def __str__(self):
    return self.name
