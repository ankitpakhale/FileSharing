
from ipaddress import ip_address
from django.db import models
# Create your models here.

class FileList(models.Model):
    files=models.FileField(upload_to ='Document/',blank=True,null=True,max_length=100)
    uploaded_by=models.CharField(max_length=50,default='')
    recieved_from=models.CharField(max_length=50,default='')
    
    def __str__(self):
        return str(self.files)    

class UserDetails2(models.Model):

    name = models.CharField(max_length=30, default='')
    email = models.EmailField(default='')
    number = models.PositiveIntegerField()
    password = models.CharField(default='', max_length=15)
    userfiles= models.ManyToManyField(FileList)
    
    def __str__(self):
        return self.name

class Ip(models.Model):
    ipaddress=models.CharField(max_length=350,default='')
    
    def __str__(self):
        return str(self.ipaddress)          


class ContactForm(models.Model):
    name = models.CharField(max_length=30, default='')
    email = models.EmailField(default='')
    subject = models.CharField(max_length=100, default='')
    message = models.CharField(max_length=1000, default='')
    
    def __str__(self):
        return self.name