
from django.test import TestCase
from django.urls import reverse
from django.conf import settings
from rest_framework.test import APIClient

from main.models import City
from main.services.city_create import city_create


class ProjectCreateTestTests(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.cities_list_url = reverse("main:create")

        self.city_data = {
            'name': 'Los Angeles, CA',
            'lat': 34.052235,
            'lon': -118.243683,
        }

    def test_create_city(self):
        """Test create city."""
        response = self.client.post(self.cities_list_url, self.city_data)
        self.assertEqual(response.status_code, 201)
        
        city = City.objects.all().first()
        self.assertEqual(city.name, 'Los Angeles, CA')
        self.assertEqual(city.lat, 34.052235)
        self.assertEqual(city.lon, -118.243683)

    def test_create_city_empty_name(self):
        """Test create city empty name."""
        self.city_data['name'] = ''
        response = self.client.post(self.cities_list_url, self.city_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["extra"]["fields"]['name'][0], 'This field may not be blank.')

    def test_create_city_empty_lat(self):
        """Test create city empty lat."""
        self.city_data['lat'] = ''
        response = self.client.post(self.cities_list_url, self.city_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["extra"]["fields"]['lat'][0], 'A valid number is required.')
    
    def test_create_city_empty_lon(self):
        """Test create city empty lon."""
        self.city_data['lon'] = ''
        response = self.client.post(self.cities_list_url, self.city_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["extra"]["fields"]['lon'][0], 'A valid number is required.')
    
    def test_create_city_empty_data(self):
        """Test create city empty data."""
        self.city_data['name'] = ''
        self.city_data['lat'] = ''
        self.city_data['lon'] = ''
        response = self.client.post(self.cities_list_url, self.city_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["extra"]["fields"]['name'][0], 'This field may not be blank.')
        self.assertEqual(response.data["extra"]["fields"]['lat'][0], 'A valid number is required.')
        self.assertEqual(response.data["extra"]["fields"]['lon'][0], 'A valid number is required.')
    
    def test_create_city_invalid_lat(self):
        """Test create city invalid lat."""
        self.city_data['lat'] = 'invalid'
        response = self.client.post(self.cities_list_url, self.city_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["extra"]["fields"]['lat'][0], 'A valid number is required.')

    def test_create_city_invalid_lon(self):
        """Test create city invalid lon."""
        self.city_data['lon'] = 'invalid'
        response = self.client.post(self.cities_list_url, self.city_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["extra"]["fields"]['lon'][0], 'A valid number is required.')

    def test_duplicate_name(self):
        """Test duplicate city."""
        city_create(**self.city_data)

        response = self.client.post(self.cities_list_url, self.city_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["extra"]["fields"]['name'][0], 'City with this Name already exists.')
    
    def test_duplicate_lat_lon(self):
        """Test duplicate lat lon city."""
        city_create(**self.city_data)
        self.city_data['name'] = 'Los Angeles, CA 2'

        response = self.client.post(self.cities_list_url, self.city_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["extra"]["fields"]['__all__'][0], 'City with this Lat and Lon already exists.')
    
