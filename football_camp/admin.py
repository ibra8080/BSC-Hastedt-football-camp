from django.contrib import admin
from .models import Service, Player, Booking
from django_summernote.admin import SummernoteModelAdmin


class ServiceAdmin(SummernoteModelAdmin):  
    summernote_fields = ('features',)  




# Register your models here.

admin.site.register(Player)
admin.site.register(Booking)
admin.site.register(Service, ServiceAdmin)


