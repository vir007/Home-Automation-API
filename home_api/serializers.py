from rest_framework import serializers
from home.models import Home, Room, Lights
from home.models import Log_thermostat, Log_lights, Log_room_temp


class LogThermostatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log_thermostat
        fields = ['home', 'oldVal', 'newVal', 'created_on']


class LogRoomTempSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log_room_temp
        fields = ['room', 'oldVal', 'newVal', 'created_on']


class LogLightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log_lights
        fields = ['lights', 'oldVal', 'newVal', 'created_on']


# Lights Serializer
class LightsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    def update(self, instance, validated_data):
        status = validated_data.get('status', None)

        if status is not None and status != instance.status:
            Log_lights.objects.create(
                lights=instance,
                oldVal=instance.status,
                newVal=status
                )

        instance.name = validated_data.get("name", instance.name)
        instance.status = validated_data.get("status", instance.status)
        instance.room = validated_data.get("room", instance.room)
        instance.save()
        return instance

    class Meta:
        model = Lights
        fields = ['id', 'name', 'status', 'room']


# Room Serializer
class RoomSerializer(serializers.ModelSerializer):
    lights = LightsSerializer(many=True, default=[])
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Room
        fields = ['id', 'name', 'temp', 'home', 'lights']

    def create(self, validated_data):
        lights_data = validated_data.pop('lights')
        room = Room.objects.create(**validated_data)

        for track_data in lights_data:
            Lights.objects.create(room=room, **track_data)
        return room

    def update(self, instance, validated_data):
        temp = validated_data.get('temp', None)

        if temp is not None and temp != instance.temp:
            Log_room_temp.objects.create(
                room=instance,
                oldVal=instance.temp,
                newVal=temp
                )

        if validated_data.get("lights", None):
            lights_data = validated_data.pop('lights')

        instance.name = validated_data.get("name", instance.name)
        instance.temp = validated_data.get("temp", instance.temp)
        instance.home = validated_data.get("home", instance.home)

        instance.save()
        return instance


# Home Serializer
class HomeSerializer(serializers.ModelSerializer):
    room = RoomSerializer(many=True, default=[])

    class Meta:
        model = Home
        fields = ['id', 'name', 'owner', 'thermostat_temp',
                  'thermostat_mode', 'room']

    def create(self, validated_data):
        room_data = validated_data.pop('room')
        home = Home.objects.create(**validated_data)

        for room_data1 in room_data:
            Room.objects.create(home=home, **room_data1)
        return home

    def update(self, instance, validated_data):
        thermostate = validated_data.get('thermostat_mode', None)

        if thermostate and thermostate != instance.thermostat_mode:
            Log_thermostat.objects.create(
                home=instance,
                oldVal=instance.thermostat_mode,
                newVal=thermostate
                )

        if validated_data.get("room", None):
            room_data = validated_data.pop('room')

        instance.name = validated_data.get("name", instance.name)
        instance.owner = validated_data.get("owner", instance.owner)
        instance.thermostat_temp = validated_data.get(
            "thermostat_temp",
            instance.thermostat_temp
            )
        instance.thermostat_mode = validated_data.get(
            "thermostat_mode",
            instance.thermostat_mode
            )
        instance.save()
        return instance
        # return super(HomeSerializer, self).update(instance, validated_data)
