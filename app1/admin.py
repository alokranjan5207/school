from django.contrib import admin
from .models import Student
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['Student_Name','Teacher_Name','Mother_Name','Adhar_No','Contact_No','Subject','Address','Salary']
