from django.db import models
import datetime
# Create your models here.
class Area(models.Model):
    name= models.CharField(max_length=10)
    area= models.CharField(max_length=10)
    building= models.CharField(max_length=15)
    floor= models.IntegerField()
    category= models.CharField(max_length=10)
    class Meta:
        db_table='Area'

PROMISSION_CHOICES= [
    ('A', 'Administer'),
    ('R', 'RegionSupervisor'),
    ('N', 'Normal'),
]

class Account(models.Model):
    name= models.CharField(max_length=10)
    account= models.CharField(max_length=20, primary_key= True, unique=True)
    jobTitle= models.CharField(max_length=10)
    serviceUnits= models.CharField(max_length=10)
    emailAddr= models.EmailField(max_length=45)
    permissions= models.CharField(max_length=1, choices=PROMISSION_CHOICES)
    activation= models.BooleanField(default=False)
    password= models.CharField(max_length=20)
    class Meta:
        db_table='Account'


class Account_Control_Area(models.Model):
    account= models.ForeignKey(Account, on_delete= models.CASCADE)
    area= models.ForeignKey(Area, on_delete= models.CASCADE)
    class Meta:
        db_table='Account_Control_Area'


class Electricity(models.Model):
    UUID= models.CharField(max_length=8)
    connection= models.BooleanField(default=False)
    current= models.DecimalField(max_digits=9, decimal_places=2)
    voltage= models.DecimalField(max_digits=9, decimal_places=2)
    power= models.DecimalField(max_digits=9, decimal_places=2)
    KwH= models.DecimalField(max_digits=9, decimal_places=2)
    mode= models.BooleanField(default=False)
    time= models.DateTimeField(default=datetime.datetime.now())
    class Meta:
        db_table='Electricity'

