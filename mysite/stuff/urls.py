from django.urls import path 
from  . import views

app_name = 'stuffs'
# Create your views here.
urlpatterns=[
    path('',views.index,name='index'),
    path('stuff/signup_stuff',views.signup_stuff,name='signup_stuff'),
    path('stuff/signup_stuff_output',views.signup_stuff_output,name='signup_stuff_output'),
    path('signin',views.signin,name = 'signin'),
    path('signin_output',views.signin_output,name = 'signin_output'),
    path('ElectricList',views.Show_Electricity, name = 'ElectricList'),
    path('main',views.main_page,name='main_page')
]

