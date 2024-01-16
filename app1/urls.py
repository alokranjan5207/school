from django.urls import path
from app1 import views
app_name='app1' #access another page by link
urlpatterns = [
    path('header/',view=views.header,name='header'),
    path('',view=views.home,name='home'),
    path('about/',view=views.about,name='about'),
    path('event/',view=views.event,name='event'),
    path('contact/',view=views.contact,name='contact'),
    path('admission/',view=views.admission,name='admission'),
    path('login/',view=views.login,name='login'),
    path('formdata/',view=views.formdata,name='formdata'),
    # path('delete/<int:id>/',view=views.delete_data,name='deletedata'),
]
