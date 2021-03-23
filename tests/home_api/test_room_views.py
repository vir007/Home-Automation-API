import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from home.models import Home, Room, Lights

UserModel = get_user_model()


class APIAdminAPITestCase(APITestCase):
    @pytest.mark.django_db
    def setUp(self):
        self.user = UserModel.objects.create_superuser(
            username='test', email='test@...', password='top_secret')
        token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)


class APIUserAPITestCase(APITestCase):
    @pytest.mark.django_db
    def setUp(self):
        self.user = UserModel.objects.create_user(
            username='test', email='test@...', password='top_secret')
        token = Token.objects.create(user= self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ token.key)


class TestRooms(APITestCase):
    @pytest.mark.django_db
    def test_anyone_can_get_rooms_list(self):
        """
        Everyone can view all room objects.
        """
        url = reverse('home_api:room_list_create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestRoomListAdmin(APIAdminAPITestCase):
    @pytest.mark.django_db
    def test_only_admin_can_post_new_room(self):
        url1 = reverse('home_api:home_list_create')
        home_data = {
            "name": "api testing home list",
            "owner": UserModel.objects.all().first().id,
            "thermostat_temp": 10,
            "thermostat_mode": "off"
        }
        response = self.client.post(url1, home_data, format='json')
        h_id = response.data['id']

        url = reverse('home_api:room_list_create')

        room_data = {
            "name": "api testing room list",
            "temp": 10,
            "home": h_id
        }
        response = self.client.post(url, room_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Anonymous User cannot post a room
        self.client.logout()
        response = self.client.post(url, room_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TestRoomDetailAnonymous(APIAdminAPITestCase):
    @pytest.mark.django_db
    def test_anyone_can_get_room_detail(self):
        url1 = reverse('home_api:home_list_create')
        home_data = {
            "name": "api testing home list",
            "owner": UserModel.objects.all().first().id,
            "thermostat_temp": 10,
            "thermostat_mode": "off"
        }
        response = self.client.post(url1, home_data, format='json')
        h_id = response.data['id']

        url = reverse('home_api:room_list_create')

        room_data = {
            "name": "api testing room list",
            "temp": 10,
            "home": h_id
        }

        response = self.client.post(url, room_data, format='json')
        r_id = response.data['id']
        self.client.logout()
        url2 = reverse('home_api:room_detail_update', kwargs={'room_id':r_id})
        response = self.client.get(url2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestRoomDetailAdmin(APIAdminAPITestCase):
    @pytest.mark.django_db
    def test_only_admin_can_delete_a_room(self):
        url1 = reverse('home_api:home_list_create')
        home_data = {
            "name": "api testing home list",
            "owner": UserModel.objects.all().first().id,
            "thermostat_temp": 10,
            "thermostat_mode": "off"
        }
        response = self.client.post(url1, home_data, format='json')
        h_id = response.data['id']

        url = reverse('home_api:room_list_create')

        room_data = {
            "name": "api testing room list",
            "temp": 10,
            "home": h_id
        }
        response = self.client.post(url, room_data, format='json')
        r_id = response.data['id']
        url2 = reverse('home_api:room_detail_update',
                       kwargs={'room_id': r_id})
        response = self.client.delete(url2)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Anonymous User cannot delete a room
        self.client.logout()
        response = self.client.delete(url2)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    @pytest.mark.django_db
    def test_only_admin_can_update_a_room(self):
        url1 = reverse('home_api:home_list_create')
        home_data = {
            "name": "api testing home list",
            "owner": UserModel.objects.all().first().id,
            "thermostat_temp": 10,
            "thermostat_mode": "off"
        }
        response = self.client.post(url1, home_data, format='json')
        h_id = response.data['id']

        url = reverse('home_api:room_list_create')

        room_data = {
            "name": "api testing room list",
            "temp": 10,
            "home": h_id
        }
        response = self.client.post(url, room_data, format='json')
        r_id = response.data['id']
        url2 = reverse('home_api:room_detail_update',
                       kwargs={'room_id': r_id})

        room_updated_data = {
            "name": "api testing room data updated",
            "temp": 15,
            "home": h_id
        }
        response = self.client.put(url2, room_updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'],
                         'api testing room data updated')
        self.assertEqual(response.json()['temp'],15)
        self.assertEqual(
            response.json()['home'], h_id)

        # Anonymous User cannot update a room
        self.client.logout()
        response = self.client.put(url2, room_updated_data, format='json')
        self.assertEqual(response.status_code,
                         status.HTTP_401_UNAUTHORIZED)

    @pytest.mark.django_db
    def test_only_admin_can_patch_a_room(self):
        url1 = reverse('home_api:home_list_create')
        home_data = {
            "name": "api testing home list",
            "owner": UserModel.objects.all().first().id,
            "thermostat_temp": 10,
            "thermostat_mode": "off"
        }
        response = self.client.post(url1, home_data, format='json')
        h_id = response.data['id']

        url = reverse('home_api:room_list_create')

        room_data = {
            "name": "api testing room list",
            "temp": 10,
            "home": h_id
        }
        response = self.client.post(url, room_data, format='json')
        r_id = response.data['id']
        url2 = reverse('home_api:room_detail_update',
                       kwargs={'room_id':r_id})

        room_updated_data = {
            "name": "api testing room data updated"
        }
        response = self.client.patch(url2, room_updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'],
                         'api testing room data updated')
        self.assertEqual(response.json()['temp'],10)
        self.assertEqual(
            response.json()['home'], h_id)

        # Anonymous User cannot patch a room
        self.client.logout()
        response = self.client.patch(url2,
                                     room_updated_data, format='json')
        self.assertEqual(response.status_code,
                         status.HTTP_401_UNAUTHORIZED)

        
