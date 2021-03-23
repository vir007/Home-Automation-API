from django.urls import path
from .views import HomeList, HomeDetail, RoomDetail
from .views import RoomList, LightsDetail, LightsList
from .views import LogLightsList, LogRoomTempList, LogThermostatList


app_name = 'home_api'

urlpatterns = [

    # Home Routes
    path('', HomeList.as_view(), name='home_list_create'),
    path('<int:home_id>/',
         HomeDetail.as_view(),
         name='home_detail_update'
         ),

    # Room Routes
    path('rooms', RoomList.as_view(), name='room_list_create'),
    path('rooms/<int:room_id>/',
         RoomDetail.as_view(),
         name='room_detail_update'
         ),
    path('<int:home_id>/<int:room_id>/',
         RoomDetail.as_view(),
         name='room_detail_update'
         ),

    # Lights Routes
    path('lights', LightsList.as_view(), name='light_room_list_create'),
    path('lights/<int:light_id>/',
         LightsDetail.as_view(),
         name='light_room_detail_update'
         ),
    path('<int:home_id>/<int:room_id>/<int:light_id>/',
         LightsDetail.as_view(),
         name='light_room_detail_update'
         ),

    # Log Tables Route
    path('loglights', LogLightsList.as_view(),
         name='log_light_list_create'
         ),
    path('logthermostat',
         LogThermostatList.as_view(),
         name='log_thermostat_list_create'
         ),
    path('logroomtemp',
         LogRoomTempList.as_view(),
         name='log_room_temp_list_create'
         ),
]
