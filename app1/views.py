from django.shortcuts import render,HttpResponseRedirect
from .models import Student,Teacher
from .forms import StudentForm,TeacherForm,LoginForm
from django.core import validators

# Create your views here.
def header(request):
    return render(request=request,template_name='header.html')

def home(request):
    return render(request=request,template_name='home.html')

def about(request):
    return render(request=request,template_name='about.html')

def event(request):
    return render(request=request,template_name='event.html')

def login(request):
    return render(request=request,template_name='login.html')

def contact(request):
    return render(request=request,template_name='contact.html')

def admission(request):
    return render(request=request,template_name='admission.html')

# def login(request):
#     return render(request=request,template_name='login.html')

# add data using form
def formdata(request):
    if request.method=='POST':
        fm=StudentForm(request.POST)
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
        fm=StudentForm()
    else:
        fm=StudentForm()
    stud=Student.objects.all()    # show all formdata
    return render(request=request,template_name='1.html',context={'form':fm,'stu':stud})

    # delete data
def delete_data(request,id):
    if request.method=='POST':
        pi=Student.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/') #delete from home


#udpate or edit
def update_data(request,id):
    if request.method=='POST':
        pi=Student.objects.get(pk=id)
        fm=StudentForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=Student.objects.get(pk=id)
        fm=StudentForm(instance=pi)
    return render(request=request,template_name='update.html',context={'form':fm})




#Teacher model
def teacherdata(request):
    if request.method=='POST':
        fm=TeacherForm(request.POST)
        if fm.is_valid():
            fm.save() #sort way to save
        
            return render(request=request,template_name="sucessfuladmsn.html")
        fm=TeacherForm()
    else:
        fm=TeacherForm()
    stud=Teacher.objects.all()    # show all formdata
    return render(request=request,template_name='2.html',context={'form':fm,'stu':stud})

    # delete data
def delete_data(request,id):
    if request.method=='POST':
        pi=Teacher.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/') #delete from home


#udpate or edit
def update_data(request,id):
    if request.method=='POST':
        pi=Teacher.objects.get(pk=id)
        fm=TeacherForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=Teacher.objects.get(pk=id)
        fm=TeacherForm(instance=pi)
    return render(request=request,template_name='update.html',context={'form':fm})






   #form details
#Student details
def student(request):
    if request.method=='POST':
        fm=StudentForm(request.POST)
        fm=(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm=StudentForm()
    return render(request=request,template_name='teacher.html',context={'form':fm})


#teacher details
def teacher(request):
    if request.method=='POST':
        fm=TeacherForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm=TeacherForm()
    return render(request=request,template_name='teacher.html',context={'form':fm})

#login
# def login(request):
#     if request.method=='POST':
#         fm=LoginForm(request.POST)
#         if fm.is_valid():
#             fm.save()
#     else:
#         fm=LoginForm()
#     return render(request=request,template_name='login.html',context={'form':fm})

#class Dropdown
def cls1(request):
    return render(request=request,template_name='cls1.html')

def cls2(request):
    return render(request=request,template_name='cls2.html')

def cls3(request):
    return render(request=request,template_name='cls3.html')

def cls4(request):
    return render(request=request,template_name='cls4.html')

def cls5(request):
    return render(request=request,template_name='cls5.html')