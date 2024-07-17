from django.contrib import admin
from .models import Userdata,Roominfo,Bookinginfo

# Register your models here.

admin.site.register(Userdata)
admin.site.register(Roominfo) 
admin.site.register(Bookinginfo) 