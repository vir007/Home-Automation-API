from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Root Model to Store the home object


class Home(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='home_owner', default=1)
    thermostat_modes = (
        ('off', 'off'), ('cool', 'cool'),
        ('heat', 'heat'), ('fan-on', 'fan-on'), ('auto', 'auto')
    )
    thermostat_temp = models.IntegerField(default=10)
    thermostat_mode = models.CharField(
        max_length=10, choices=thermostat_modes, default='off')
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created_on',)

# Model to Store the room object


class Room(models.Model):
    name = models.CharField(max_length=100)
    home = models.ForeignKey(
        Home,
        related_name='room',
        on_delete=models.CASCADE)
    temp = models.IntegerField(default=10)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created_on',)

# Model to Store the light object


class Lights(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    room = models.ForeignKey(
        Room,
        related_name='lights',
        on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created_on',)

# Model to Track the change of home thermostate mode, ie. "off"->"fan-on"


class Log_thermostat(models.Model):
    home = models.ForeignKey(
        Home,
        related_name='home_thermostate',
        on_delete=models.CASCADE)
    oldVal = models.CharField(max_length=100)
    newVal = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created_on',)

# Model to Track the change of light status, ie. True -> Flase, False-> True


class Log_lights(models.Model):
    lights = models.ForeignKey(
        Lights,
        related_name='lights_log',
        on_delete=models.CASCADE)
    oldVal = models.CharField(max_length=100)
    newVal = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created_on',)

# Model to Track the change of room temperature value, ie. 10 -> 15


class Log_room_temp(models.Model):
    room = models.ForeignKey(
        Room,
        related_name='room_temp',
        on_delete=models.CASCADE)
    oldVal = models.CharField(max_length=100)
    newVal = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created_on',)
