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
    path('formdata/',view=views.formdata,name='formdata'),
    # path('teacherdata/',view=views.teacherdata,name='teacherdata'),

    # path('delete/<int:id>/',view=views.delete_data,name='deletedata'),
    path('teacher/',view=views.teacher,name='teacher'),
    path('student/',view=views.student,name='student'),
    path('login/',view=views.login,name='login'),
    #syllabus dropwown
    path('cls1/',view=views.cls1,name='cls1'),
    path('cls2/',view=views.cls2,name='cls2'),
    path('cls3/',view=views.cls3,name='cls3'),
    path('cls4/',view=views.cls4,name='cls4'),
    path('cls5/',view=views.cls5,name='cls5'),


]
