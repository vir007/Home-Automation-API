import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from home.models import Home,Room,Lights

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

class TestHomeListAnonymous(APITestCase):
    @pytest.mark.django_db
    def test_anyone_can_get_home_list(self):
        """
        Everyone can view all home objects.
        """
        url = reverse('home_api:home_list_create')
        response = self.client.get(url,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TestHomeListAdmin(APIAdminAPITestCase):
    @pytest.mark.django_db
    def test_only_admin_can_post_new_home(self):
        url = reverse('home_api:home_list_create')

        home_data = {
            "name": "api testing home list",
            "owner": 1,
            "thermostat_temp": 10,
            "thermostat_mode": "off"
        }
        response = self.client.post(url, home_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.client.logout()
        # Anonymous User Cannot post a home
        response = self.client.post(url, home_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
class TestHomeDetailAnonymous(APIAdminAPITestCase):
    @pytest.mark.django_db
    def test_anyone_can_get_home_detail(self):
        url1 = reverse('home_api:home_list_create')
        home_data = {
            "name": "api testing home list",
            "owner": UserModel.objects.all().first().id,
            "thermostat_temp": 10,
            "thermostat_mode": "off"
        }
        response = self.client.post(url1, home_data, format='json')
        h_id=response.data['id']
        self.client.logout()
        url2 = reverse('home_api:home_detail_update', kwargs={'home_id':h_id})
        response = self.client.get(url2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TestHomeDetailAdmin(APIAdminAPITestCase):
    @pytest.mark.django_db
    def test_only_admin_can_delete_a_home(self):
        url1 = reverse('home_api:home_list_create')
        home_data = {
            "name": "api testing home list",
            "owner": UserModel.objects.all().first().id,
            "thermostat_temp": 10,
            "thermostat_mode": "off"
        }
        response = self.client.post(url1, home_data, format='json')
        h_id=response.data['id']
        url2 = reverse('home_api:home_detail_update', kwargs={'home_id':h_id})
        response = self.client.delete(url2)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Anonymous User cannot delete a home
        self.client.logout()
        response = self.client.delete(url2)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    @pytest.mark.django_db
    def test_only_admin_can_update_a_home(self):
        url1 = reverse('home_api:home_list_create')
        home_data = {
            "name": "api testing home list",
            "owner": UserModel.objects.all().first().id,
            "thermostat_temp": 10,
            "thermostat_mode": "off"
        }
        response = self.client.post(url1, home_data, format='json')
        h_id = response.data['id']
        url2 = reverse('home_api:home_detail_update', kwargs={'home_id': h_id})
        home_updated_data = {
            "name": "api testing home list updated",
            "owner": UserModel.objects.all().first().id,
            "thermostat_temp": 100,
            "thermostat_mode": "auto"
        }
        response = self.client.put(url2, home_updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], 'api testing home list updated')
        self.assertEqual(
            response.json()['thermostat_mode'], 'auto')
        self.assertEqual(
            response.json()['thermostat_temp'], 100)

        # Anonymous User cannot update a home
        self.client.logout()
        response = self.client.put(url2, home_updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    @pytest.mark.django_db
    def test_only_admin_can_patch_a_home(self):
        url1 = reverse('home_api:home_list_create')
        home_data = {
            "name": "api testing home list",
            "owner": UserModel.objects.all().first().id,
            "thermostat_temp": 10,
            "thermostat_mode": "off"
        }
        response = self.client.post(url1, home_data, format='json')
        h_id = response.data['id']
        url2 = reverse('home_api:home_detail_update', kwargs={'home_id': h_id})
        home_updated_data = {
            "name": "api testing home list updated",
        }
        response = self.client.patch(url2, home_updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], 'api testing home list updated')
        self.assertEqual(
            response.json()['thermostat_mode'], 'off')
        self.assertEqual(
            response.json()['thermostat_temp'], 10)
        
        # Anonymous User cannot patch a home
        self.client.logout()
        response = self.client.patch(url2, home_updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
