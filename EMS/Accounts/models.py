from django.db import models

# Create your models here.
class Stuff(models.Model):
    
    PERMISSION_CHOICES= [
        ('A', '管理員'),
        ('R', '區域負責人'),
        ('N', '一般使用者'),
    ]
    ACTIVATION_CHOICES= [
        (True, '啟用'),
        (False, '停用'),
    ]

    name = models.CharField(max_length=20)
    account = models.CharField(max_length=20,unique=True)
    title = models.CharField(max_length=20)
    unit = models.CharField(max_length=20)
    email = models.EmailField()
    permission = models.CharField(max_length=1, choices=PERMISSION_CHOICES)
    activation= models.BooleanField(default=False, choices=ACTIVATION_CHOICES)

    class Meta:
        
        db_table='Stuff'
        permissions = (
            ("Admin", "管理人"),
            ("Region", "區域負責人"),
            ("Normal", "一般使用者"),
        )