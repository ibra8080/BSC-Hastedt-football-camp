from django.contrib import admin
from .models import Service, Player, Booking

# Register your models here.

admin.site.register(Service)
admin.site.register(Player)
admin.site.register(Booking)
