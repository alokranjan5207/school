from django.shortcuts import render,HttpResponseRedirect
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
# add data using form
def formdata(request):
    if request.method=='POST':
        fm=AdmissionForm(request.POST)
        if fm.is_valid():
            fm.save() #sort way to save
        # if fm.is_valid():
        #     nm=fm.changed_data['Student_Name']
        #     mn=fm.cleaned_data['Mother_Name']
        #     adrn=fm.cleaned_data['Adhar_No']
        #     cnt=fm.cleaned_data['Contact_No']
        #     adrs=fm.cleaned_data['Address']
        #     res=AdmissionForm(Student_Name=nm,Mother_Name=mn,Adhar_No=adrn,Contact_No=cnt,Address=adrs)
        #     res.save()
            return render(request=request,template_name="sucessfuladmsn.html")
        fm=AdmissionForm()
    else:
        fm=AdmissionForm()
    stud=Admission.objects.all()    # show all formdata
    return render(request=request,template_name='1.html',context={'form':fm,'stu':stud})

    # delete data
def delete_data(request,id):
    if request.method=='POST':
        pi=Admission.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/') #delete from home


#udpate or edit
def update_data(request,id):
    if request.method=='POST':
        pi=Admission.objects.get(pk=id)
        fm=AdmissionForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=Admission.objects.get(pk=id)
        fm=AdmissionForm(instance=pi)
    return render(request=request,template_name='update.html',context={'form':fm})
