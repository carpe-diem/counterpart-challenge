
from django.test import TestCase
from django.urls import reverse
from django.conf import settings
from rest_framework.test import APIClient

from main.models import City
from main.tests.factories import CityFactory


class ProjectListTestTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.cities_list_url = reverse("main:list")

        for x in range(3):
            CityFactory()
    
    def test_list_cities(self):
        """Test list cities."""
        response = self.client.get(self.cities_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]['name'], 'Test City Name 0')
        self.assertEqual(response.data[1]['name'], 'Test City Name 1')
        self.assertEqual(response.data[2]['name'], 'Test City Name 2')
    
    def test_list_cities_empty(self):
        """Test list cities empty."""
        CityFactory.reset_sequence()
        City.objects.all().delete()
        response = self.client.get(self.cities_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)
