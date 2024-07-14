from django.contrib import admin
from .models import Service, Player, Booking
from django_summernote.admin import SummernoteModelAdmin


class ServiceAdmin(SummernoteModelAdmin):  
    summernote_fields = ('features',)  

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'focus', 'duration', 'training')
    fields = ('title', 'focus', 'duration', 'features', 'training', 'image')


# Register your models here.

admin.site.register(Player)
admin.site.register(Booking)
admin.site.register(Service, ServiceAdmin)


