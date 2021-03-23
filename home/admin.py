from django.contrib import admin
from . import models

# Registeration of major models to the admin.
admin.site.register(models.Home)
admin.site.register(models.Room)
admin.site.register(models.Lights)
