from django.contrib import admin
from .models import Student,Teacher
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['Student_Name','Teacher_Name','Mother_Name','Adhar_No','Contact_No','Subject','Address','Salary']
    # list_display=['Student_Name','Class','Mother_Name','Address','Contact_No','Adhar_No']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    # list_display=['Teacher_Name','Subject','Salary','Address','Contact_NO','Adhar_No']
    list_display=['Teacher','Subject','Contact']
