from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from .models import Account, Electricity
from django.urls import reverse
import json
from django.core import serializers

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
    tempBlogs = []
    latest_electricity_list = Electricity.objects.all()
    
    context = {
        'latest_electricity_list': latest_electricity_list.values('UUID', 'KwH'),
        'msg':{'name':['Dongle用電量','Device用電量']}
    }
    for i in range(len(latest_electricity_list)):
        tempBlogs.append(blogToDictionary(latest_electricity_list[i])) # Converting `QuerySet` to a Python Dictionary


    print(json.dumps(tempBlogs))
    jsondata = dict()
    weather={
	    "describe": "晴時多雲", 
	    "date": "2022-09-04", 
	    "day": "Mon",         
	    "temp": 28,           
	    "humid": 60,          
	    "wind": 8             
    }
    total_electricity={
        "instant_power_usage": 0000.0, 
        "contract_capacity": 0000.0,    
        "today_electricity": 0000.0,    
        "year_electricity": 0000.0,    
    }
    jsondata["weather"]=weather
    jsondata["total_electricity"]=weather
    print(json.dumps(jsondata))

    return render(request, 'ElectricList.html', context)

def blogToDictionary(blog):
    """
    A utility function to convert object of type Blog to a Python Dictionary
    """
    output = {}
    output["UUID"] = blog.UUID
    output["KwH"] = blog.KwH

    return output

