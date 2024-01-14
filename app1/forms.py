from django import forms
from .models import Admission
from django.core import validators

class AdmissionForm(forms.ModelForm):
    class Meta:
        model=Admission
        fields=['Student_Name','Mother_Name','Adhar_No','Contact_No','Address']
        widgets={
            'Student_Name':forms.TextInput(attrs={'class':'form-control'}),
            'Mother_Name':forms.TextInput(attrs={'class':'form-control'}),
            'Adhar_No':forms.TextInput(attrs={'class':'form-control'}),
            'Contact_No':forms.TextInput(attrs={'class':'form-control'}),
            'Address':forms.TextInput(attrs={'class':'form-control'}),




        }