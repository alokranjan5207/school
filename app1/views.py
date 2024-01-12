from django.shortcuts import render
from .models import Admission
from .forms import AdmissionForm
# Create your views here.
def header(request):
    return render(request=request,template_name='header.html')

def home(request):
    return render(request=request,template_name='home.html')

def about(request):
    return render(request=request,template_name='about.html')

def event(request):
    return render(request=request,template_name='event.html')

def contact(request):
    return render(request=request,template_name='contact.html')

def admission(request):
    return render(request=request,template_name='admission.html')

def login(request):
    return render(request=request,template_name='login.html')

def formdata(request):
    if request.method=='POST':
        fm=AdmissionForm(request.POST)
        if fm.is_valid():
            nm=int(fm.changed_data['Student_Name'])
            mn=fm.cleaned_data['Mother_Name']
            adrn=fm.cleaned_data['Adhar_No']
            cnt=fm.cleaned_data['Contact_No']
            adrs=fm.cleaned_data['Address']
            res=AdmissionForm(Student_Name=nm,Mother_Name=mn,Adhar_No=adrn,Contact_No=cnt,Address=adrs)
            res.save()
            fm=AdmissionForm()
    else:
        fm=AdmissionForm()
    return render(request=request,template_name='1.html')