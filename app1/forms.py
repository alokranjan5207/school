from django import forms
from .models import Admission
from django.core import validators

class AdmissionForm(forms.Form):
    class Meta:
        model=Admission
        fields=['Student_Name','Mother_Name','Adhar_No','Contact_No','Address']