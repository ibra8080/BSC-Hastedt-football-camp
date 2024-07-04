from django.contrib import admin
from .models import Service, Player, Booking


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'focus', 'duration', 'training')


# Register your models here.

admin.site.register(Player)
admin.site.register(Booking)
admin.site.register(Service, ServiceAdmin)


