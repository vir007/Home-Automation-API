from rest_framework import generics
from .permissions import IsAdminOrReadOnly
from home.models import Home, Room, Lights, Log_lights, Log_room_temp,Log_thermostat
from .serializers import HomeSerializer,RoomSerializer,LightsSerializer,LogLightsSerializer,LogThermostatSerializer,LogRoomTempSerializer

# GET   : Retrive All Home Objects --Permission: Anyone
# POST  : Create new Home Object --Permission: OnlyAdmin
class HomeList(generics.ListCreateAPIView):
    queryset = Home.objects.all() 
    serializer_class = HomeSerializer
    permission_classes = (IsAdminOrReadOnly,)
    lookup_url_kwarg = 'home_id'

# GET   : Retrieve a Home Object --Permission: Anyone
# PUT   : Update all fields of a Home Object --Permission: OnlyAdmin
# PATCH : Update perticular field of a Home Object --Permission: OnlyAdmin  
# DELETE: Destroy a Home Object --Permission: OnlyAdmin
class HomeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer
    permission_classes = (IsAdminOrReadOnly,)
    lookup_url_kwarg = 'home_id'

# GET   : Retrive All Room Objects --Permission: Anyone
# POST  : Create a new Room Object --Permission: OnlyAdmin
class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all() 
    serializer_class = RoomSerializer
    permission_classes = (IsAdminOrReadOnly,)
    lookup_url_kwarg = 'room_id'

# GET   : Retrieve a Room Object --Permission: Anyone
# PUT   : Update all fields of a Room Object --Permission: OnlyAdmin
# PATCH : Update a perticular field of a Room Object --Permission: OnlyAdmin  
# DELETE: Destroy a Room Object --Permission: OnlyAdmin
class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (IsAdminOrReadOnly,)
    lookup_url_kwarg = 'room_id'

# GET   : Retrive All Lights Objects --Permission: Anyone
# POST  : Create a new Lights Object --Permission: OnlyAdmin
class LightsList(generics.ListCreateAPIView):
    queryset = Lights.objects.all() 
    serializer_class = LightsSerializer
    permission_classes = (IsAdminOrReadOnly,)
    lookup_url_kwarg = 'light_id'

# GET   : Retrieve a Lights Object --Permission: Anyone
# PUT   : Update all fields of a Lights Object --Permission: OnlyAdmin
# PATCH : Update a perticular field of a Lights Object --Permission: OnlyAdmin  
# DELETE: Destroy a Lights Object --Permission: OnlyAdmin
class LightsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lights.objects.all()
    serializer_class = LightsSerializer
    permission_classes = (IsAdminOrReadOnly,)
    lookup_url_kwarg = 'light_id'

class LogLightsList(generics.ListCreateAPIView):
    queryset = Log_lights.objects.all()
    serializer_class = LogLightsSerializer
    permission_classes = (IsAdminOrReadOnly,)
    # lookup_url_kwarg = 'light_id'

class LogThermostatList(generics.ListCreateAPIView):
    queryset = Log_thermostat.objects.all()
    serializer_class = LogThermostatSerializer
    permission_classes = (IsAdminOrReadOnly,)

class LogRoomTempList(generics.ListCreateAPIView):
    queryset = Log_room_temp.objects.all()
    serializer_class = LogRoomTempSerializer
    permission_classes = (IsAdminOrReadOnly,)