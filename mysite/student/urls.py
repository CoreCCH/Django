from django.urls import path 
from  . import views

app_name = 'students'
# Create your views here.
urlpatterns=[
    path('',views.index,name='index'),
    path('student/signup_student',views.signup_student,name='signup_student'),
    path('student/signup_student_output',views.signup_student_output,name='signup_student_output2')
]

