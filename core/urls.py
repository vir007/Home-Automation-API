from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('api/', include('home_api.urls', namespace='home_api')),
    path('api-token-auth/', obtain_auth_token),  
]