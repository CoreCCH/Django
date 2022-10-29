from django.db import models
# Create your models here.
class student(models.Model):
    name =models.CharField(max_length=100)
    cl=models.CharField(max_length=10,db_column='class')
    mark =models.IntegerField()
    gender  =models.CharField(max_length=6)
    class Meta:
        db_table='student'