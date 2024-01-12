from django.db import models

# Create your models here.
class Admission(models.Model):
    Student_Name=models.CharField(max_length=50)
    Mother_Name=models.CharField(max_length=50)
    Adhar_No=models.IntegerField()
    Contact_No=models.IntegerField(max_length=10)
    Address=models.CharField(max_length=50)

