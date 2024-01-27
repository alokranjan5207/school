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
            # 'Teacher_Name':forms.TextInput(attrs={'class':'form-control'}),
            # 'Subject':forms.TextInput(attrs={'class':'form-control'}),

            'Mother_Name':forms.TextInput(attrs={'class':'form-control'}),
            # 'Class':forms.Textarea(attrs={'class':'form-control'}),
            'Adhar_No':forms.TextInput(attrs={'class':'form-control'}),
            'Contact_No':forms.TextInput(attrs={'class':'form-control'}),
            'Address':forms.TextInput(attrs={'class':'form-control'}),
            'Salary':forms.TextInput(attrs={'class':'form-control'}),

            
        }
        fields=['Student_Name','Mother_Name','Adhar_No','Contact_No','Address','Salary']

class TeacherForm(forms.ModelForm):
    class Meta:
        model=Teacher
        # fields=['Teacher_Name','Subject','Salary','Address','Contact_No','Adhar_No']
        fields=['Teacher','Subject','Contact']



class TeacherForm(StudentForm):
    class Meta(StudentForm.Meta):
        fields=['Teacher_Name','Subject','Adhar_No','Contact_No','Address','Salary']

class LoginForm(TeacherForm):
    class Meta(TeacherForm.Meta):
        fields=['Contact_No',]
