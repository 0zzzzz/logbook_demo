from django.contrib import admin
from .models import Clients, Equipment, Modes, Durations

admin.site.register(Clients)
admin.site.register(Equipment)
admin.site.register(Modes)
admin.site.register(Durations)