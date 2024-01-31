from .models import Student,Teacher
from django.forms import ModelForm
# from django.core import validators
from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['Student_Name','Mother_Name','Adhar_No','Contact_No','Address']
        widgets={
            'Student_Name':forms.TextInput(attrs={'class':'form-control'}),
            'Mother_Name':forms.TextInput(attrs={'class':'form-control'}),
            'Adhar_No':forms.TextInput(attrs={'class':'form-control'}),
            'Contact_No':forms.TextInput(attrs={'class':'form-control'}),
            'Address':forms.TextInput(attrs={'class':'form-control'})
        }
        fields=['Student_Name','Mother_Name','Adhar_No','Contact_No','Address']

class TeacherForm(StudentForm):
    class Meta(StudentForm.Meta):
        # fields=['Teacher_Name','Subject','Adhar_No','Contact_No','Address','Salary']
        fields=['Teacher_Name','Subject','Salary','Contact_No']


class LoginForm(TeacherForm):
    class Meta(TeacherForm.Meta):
        fields=['Contact_No',]
