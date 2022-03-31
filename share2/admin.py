from telnetlib import IP
from django.contrib import admin
from . models import *
# Register your models here.

admin.site.register(FileList)
admin.site.register(UserDetails2)
admin.site.register(Ip)