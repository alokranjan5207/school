from django.db import models

# Create your models here.
class Admission(models.Model):
    Student_Name=models.CharField(max_length=50)
    # Teacher_Name=models.CharField(max_length=40)
    Mother_Name=models.CharField(max_length=30)
    Adhar_No=models.IntegerField()
    Contact_No=models.IntegerField()
    Address=models.CharField(max_length=50)
    # Salary=models.IntegerField(max_length=6,default=10000)

