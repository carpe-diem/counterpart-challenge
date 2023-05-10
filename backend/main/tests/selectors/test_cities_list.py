from django.test import TestCase
from django.db.models.query import QuerySet

from main.models import City
from main.tests.factories import CityFactory

from main.selectors.cities_list import cities_list


class SelectorCitiesListTests(TestCase):
    """Test for cities list selector."""
    def setUp(self):
        for x in range(5):
            CityFactory(name=f'Test City Name {x}')

    def test_cities_list(self):
        """Test cities_list selector."""
        cities = cities_list()
        self.assertEqual(len(cities), 5)

    def test_cities_list_order(self):
        """Test cities_list selector order."""
        cities = cities_list()
        self.assertEqual(cities[0].name, 'Test City Name 0')
        self.assertEqual(cities[1].name, 'Test City Name 1')
        self.assertEqual(cities[2].name, 'Test City Name 2')
        self.assertEqual(cities[3].name, 'Test City Name 3')
        self.assertEqual(cities[4].name, 'Test City Name 4')
    
    def test_cities_list_type(self):
        """Test cities_list selector type."""
        cities = cities_list()
        self.assertIsInstance(cities, QuerySet)
        self.assertEqual(type(cities[0]), type(CityFactory()))

    def test_cities_list_empty(self):
        """Test cities_list selector empty."""
        City.objects.all().delete()
        cities = cities_list()
        self.assertEqual(len(cities), 0)
