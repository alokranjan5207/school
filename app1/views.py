from django.shortcuts import render

# Create your views here.
def header(request):
    return render(request=request,template_name='header.html')

def home(request):
    return render(request=request,template_name='home.html')

def about(request):
    return render(request=request,template_name='about.html')

def event(request):
    return render(request=request,template_name='event.html')