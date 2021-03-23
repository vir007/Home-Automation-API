from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Home(models.Model):
    """
    Model to Store the home object
    
    Required Parameters -
    name: name of a home object
    owner: owner of a perticular home object

    Other Parameters -
    thermostat_temp: temperature value of a thermostat
    thermostat_modes: different thermostat modes
    created_on: creation date of a home object
    """
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


class Room(models.Model):
    """
    Model to Store the room object
    
    Required Parameters -
    name: name of a room object.
    home: home_id, a room object is a part of this home object.

    Other Parameters -
    temp: temperature value of a perticular room
    created_on: creation date of a room object
    """
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


class Lights(models.Model):
    """
    Model to Store the light object

    Required Parameters -
    name: name of a light object.
    room: room_id, a light object is a part of this room object.

    Other Parameters -
    status: True if a light is on, False if a light is off.
    created_on: creation date of a light object
    """
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


class Log_thermostat(models.Model):
    """
    Model to Track the change of home thermostate mode, ie. "off"->"fan-on"

    Parameters -
    home: home_id, thermostat mode changed for this home object.
    oldVal: previous mode of a thermostat
    newVal: updated mode of a thermostat
    created_on: date and time when the mode change is occured
    """
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


class Log_lights(models.Model):
    """
    Model to Track the change of light status, ie. True -> Flase, False-> True

    Parameters -
    lights: lights_id, light status changed for this light object.
    oldVal: previous status of a light
    newVal: updated status of a light
    created_on: date and time when the status change is occured
    """
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


class Log_room_temp(models.Model):
    """
    Model to Track the change of room temperature value, ie. 10 -> 15

    Parameters -
    room: room_id, temperature status changed for this room object.
    oldVal: previous temperature of a room
    newVal: updated temperature of a room
    created_on: date and time when the temperature change is occured
    """
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
