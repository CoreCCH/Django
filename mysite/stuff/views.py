from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Account, Electricity
from django.urls import reverse
import json

# Create your views here.
def index(request):
    return render(request,'form.html')

def signup_stuff(request):
    return render(request,'signup_stuff.html',{'msg':'Stuff Signup'})
def signup_stuff_output(request):
    en=Account(name=request.POST.get('name'),account=request.POST.get('account'),
     serviceUnits=request.POST.get('serviceUnits'),emailAddr=request.POST.get('emailAddr'),
     permissions=request.POST.get('permissions'),activation=request.POST.get('activation'),
     password=request.POST.get('password'))
    en.save()
    return render(request,'signup_stuff.html')

def signin(request):
    return render(request,'signin.html',{'msg':'please sign in.'})

def signin_output(request):
    account= request.POST.get('account')
    password= request.POST.get('password')
    try:
        Stuff = Account.objects.get(account__exact=account)
    except:
        return render(request,'signin.html',{'msg':'無此帳號'})
    else:
        if(Stuff.password != password):
            return render(request,'signin.html',{'msg':'密碼有誤'})
        else:
            return HttpResponseRedirect('/stuff/main')

def main_page(request):
    return render(request,'main_page.html')

def Show_Electricity(request):
    latest_electricity_list = Electricity.objects.all()
    
    context = {
        'latest_electricity_list': latest_electricity_list,
        'msg':'Dongle用電量'
    }


    return render(request, 'ElectricList.html', context)

