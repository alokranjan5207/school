from django.contrib import admin
from app1.models import Student
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # list_display=['Student_Name','Teacher_Name','Mother_Name','Adhar_No','Contact_No','Subject','Address','Salary']

    list_display=['Student_Name','Mother_Name','Adhar_No','Contact_No','Address']

# @admin.register(Teacher)

# class TeacherAdmin(admin.ModelAdmin):
#         list_display=['Teacher_Name','Subject','Salary','Contact_No']

