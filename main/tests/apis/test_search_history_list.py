
from django.test import TestCase
from django.urls import reverse
from django.conf import settings
from rest_framework.test import APIClient

from main.models import SearchHistory
from main.tests.factories import CityFactory, SearchHistoryFactory


class ProjectListTestTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.searches_list_url = reverse("main:history-list")
        
        self.city = CityFactory(name=f'Test City Name')
        SearchHistoryFactory(city=self.city)
        SearchHistoryFactory(city=self.city)
    
    def test_list_searches(self):
        """Test list searches."""
        response = self.client.get(self.searches_list_url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['city'], self.city.name)

    
    def test_list_searches_empty(self):
        """Test list searches empty."""
        SearchHistoryFactory.reset_sequence()
        SearchHistory.objects.all().delete()

        response = self.client.get(self.searches_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)
