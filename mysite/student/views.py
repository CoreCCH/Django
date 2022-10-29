from django.shortcuts import render
from django.http import HttpResponse
from .models import student
# Create your views here.
def index(request):
    return render(request,'form.html')

def signup_student(request):
    return render(request,'signup_student.html',{'msg':'Student Signup'})
def signup_student_output(request):
    en=student(name=request.POST.get('name'),cl=request.POST.get('class'),
     mark=request.POST.get('mark'),gender=request.POST.get('gender'))
    en.save()
    str1="Data inserted to student table with id:" + str(en.id) 
    return render(request,'signup_student.html',{'msg':str1})