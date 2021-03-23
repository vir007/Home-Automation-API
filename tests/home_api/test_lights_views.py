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
        token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)


class TestLights(APITestCase):
    @pytest.mark.django_db
    def test_anyone_can_get_lights_list(self):
        """
        Everyone can view all light objects.
        """
        url = reverse('home_api:light_room_list_create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestLightsListAdmin(APIAdminAPITestCase):
    @pytest.mark.django_db
    def test_only_admin_can_post_new_light(self):
        url1 = reverse('home_api:home_list_create')
        home_data = {
            "name": "api testing home list",
            "owner": UserModel.objects.all().first().id,
            "thermostat_temp": 10,
            "thermostat_mode": "off"
        }
        response = self.client.post(url1, home_data, format='json')
        h_id = response.data['id']

        url2 = reverse('home_api:room_list_create')

        room_data = {
            "name": "api testing room list",
            "home": h_id
        }

        response = self.client.post(url2, room_data, format='json')
        r_id = response.data['id']

        light_data = {
            "name": "api testing light post",
            "status": False,
            "room": r_id
        }

        url3 = reverse('home_api:light_room_list_create')

        response = self.client.post(url3, light_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Anonymous user cannot post a new light
        self.client.logout()
        response = self.client.post(url3, light_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TestLightsDetailAnonymous(APIAdminAPITestCase):
    @pytest.mark.django_db
    def test_anyone_can_get_light_detail(self):
        url1 = reverse('home_api:home_list_create')
        home_data = {
            "name": "api testing home list",
            "owner": UserModel.objects.all().first().id,
            "thermostat_temp": 10,
            "thermostat_mode": "off"
        }
        response = self.client.post(url1, home_data, format='json')
        h_id = response.data['id']

        url2 = reverse('home_api:room_list_create')

        room_data = {
            "name": "api testing room list",
            "home": h_id
        }

        response = self.client.post(url2, room_data, format='json')
        r_id = response.data['id']

        light_data = {
            "name": "api testing light post",
            "status": False,
            "room": r_id
        }

        url3 = reverse('home_api:light_room_list_create')
        response = self.client.post(url3, light_data, format='json')
        l_id = response.data['id']

        self.client.logout()
        url4 = reverse('home_api:light_room_detail_update',
                       kwargs={'light_id': l_id})
        response = self.client.get(url4)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestRoomDetailAdmin(APIAdminAPITestCase):
    @pytest.mark.django_db
    def test_only_admin_can_delete_a_light(self):
        url1 = reverse('home_api:home_list_create')
        home_data = {
            "name": "api testing home list",
            "owner": UserModel.objects.all().first().id,
            "thermostat_temp": 10,
            "thermostat_mode": "off"
        }
        response = self.client.post(url1, home_data, format='json')
        h_id = response.data['id']

        url2 = reverse('home_api:room_list_create')

        room_data = {
            "name": "api testing room list",
            "home": h_id
        }

        response = self.client.post(url2, room_data, format='json')
        r_id = response.data['id']

        light_data = {
            "name": "api testing light post",
            "status": False,
            "room": r_id
        }

        url3 = reverse('home_api:light_room_list_create')
        response = self.client.post(url3, light_data, format='json')
        l_id = response.data['id']

        url4 = reverse('home_api:light_room_detail_update',
                       kwargs={'light_id': l_id})
        response = self.client.delete(url4)
        self.assertEqual(response.status_code,
                         status.HTTP_204_NO_CONTENT)

        # Anonymous User Cannot delete a room
        self.client.logout()
        response = self.client.delete(url4)
        self.assertEqual(response.status_code,
                         status.HTTP_401_UNAUTHORIZED)

    @pytest.mark.django_db
    def test_only_admin_can_update_a_light(self):
        url1 = reverse('home_api:home_list_create')
        home_data = {
            "name": "api testing home list",
            "owner": UserModel.objects.all().first().id,
            "thermostat_temp": 10,
            "thermostat_mode": "off"
        }
        response = self.client.post(url1, home_data, format='json')
        h_id = response.data['id']

        url2 = reverse('home_api:room_list_create')

        room_data = {
            "name": "api testing room list",
            "home": h_id
        }

        response = self.client.post(url2, room_data, format='json')
        r_id = response.data['id']

        light_data = {
            "name": "api testing light post",
            "status": False,
            "room": r_id
        }

        url3 = reverse('home_api:light_room_list_create')
        response = self.client.post(url3, light_data, format='json')
        l_id = response.data['id']

        url4 = reverse('home_api:light_room_detail_update',
                       kwargs={'light_id': l_id})

        light_updated_data = {
            "name": "api testing light put",
            "status": True,
            "room": r_id
        }

        response = self.client.put(url4, light_updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], 'api testing light put')
        self.assertEqual(
            response.json()['status'], True)
        self.assertEqual(
            response.json()['room'], r_id)

        # Anonymous User cannot update a light
        self.client.logout()
        response = self.client.put(url4, light_updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    @pytest.mark.django_db
    def test_only_admin_can_patch_a_light(self):
        url1 = reverse('home_api:home_list_create')
        home_data = {
            "name": "api testing home list",
            "owner": UserModel.objects.all().first().id,
            "thermostat_temp": 10,
            "thermostat_mode": "off"
        }
        response = self.client.post(url1, home_data, format='json')
        h_id = response.data['id']

        url2 = reverse('home_api:room_list_create')

        room_data = {
            "name": "api testing room list",
            "home": h_id
        }

        response = self.client.post(url2, room_data, format='json')
        r_id = response.data['id']

        light_data = {
            "name": "api testing light post",
            "status": False,
            "room": r_id
        }

        url3 = reverse('home_api:light_room_list_create')
        response = self.client.post(url3, light_data, format='json')
        l_id = response.data['id']

        url4 = reverse('home_api:light_room_detail_update',
                       kwargs={'light_id': l_id})

        light_updated_data = {
            "status": True
        }

        response = self.client.patch(url4, light_updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], 'api testing light post')
        self.assertEqual(
            response.json()['status'], True)
        self.assertEqual(
            response.json()['room'], r_id)

        # Anonymous User cannot patch a light
        self.client.logout()
        response = self.client.patch(url4, light_updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
