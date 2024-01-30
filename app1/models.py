from django.db import models

# Create your models here.
class Student(models.Model):
    Student_Name=models.CharField(max_length=50)
    Classs=models.IntegerField()
    Mother_Name=models.CharField(max_length=50)
    Contact_No=models.IntegerField()
    Address=models.CharField(max_length=50)    
    Adhar_No=models.IntegerField()


    # Teacher_Name=models.CharField(max_length=50)
    # Salary=models.IntegerField(max_length=50,default=10000)
    # Subject=models.CharField(max_length=30,default='maths')




# class Teacher(models.Model):
#     Teacher_Name=models.CharField(max_length=40)
#     Subject=models.CharField(max_length=30)
#     Contact_No=models.IntegerField(max_length=10)
#     #Salary=models.IntegerField(max_length=6)


# def __str__(self):
#     return self.name
def __str__(self):
    return self.name