from django.contrib import admin
from . import models
from home.models import Log_lights, Log_room_temp, Log_thermostat

# Registeration of major models to the admin.
admin.site.register(models.Home)
admin.site.register(models.Room)
admin.site.register(models.Lights)
admin.site.register(models.Log_lights)
admin.site.register(models.Log_room_temp)
admin.site.register(models.Log_thermostat)

