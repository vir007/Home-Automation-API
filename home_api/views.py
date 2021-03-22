from rest_framework import generics
from .permissions import IsAdminOrReadOnly
from home.models import Home,Room,Lights
from .serializers import HomeSerializer,RoomSerializer,LightsSerializer

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