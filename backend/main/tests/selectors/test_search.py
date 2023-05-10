from django.test import TestCase
from django.db.models.query import QuerySet

from main.exceptions import ApplicationError
from main.selectors.search import search
from main.tests.factories import CityFactory
from main.utils import format_date_from_string

class SelectorCitiesListTests(TestCase):
    """Test for cities list selector."""
    def setUp(self):
        self.city = CityFactory(name='Los Angeles, CA', lat=34.052235, lon=-118.243683)

    def test_search(self):
        """Test search selector."""
        cities = search(city=self.city,  date_from='2021-06-07', date_to='2021-07-07')
        self.assertIsInstance(cities, dict)
        self.assertEqual(cities['city'], 'Los Angeles, CA')
        self.assertEqual(cities['date_from'], format_date_from_string('2021-06-07'))
        self.assertEqual(cities['date_to'], format_date_from_string('2021-07-07'))
        self.assertEqual(cities['closest_earthquake'], 'Corral del Risco (Punta de Mita), Mexico')
        self.assertEqual(cities['magnitude'], 5.6)
        self.assertEqual(cities['date'], format_date_from_string('2021-07-04'))
    
    def test_search_empty(self):
        """Test search selector empty."""
        cities = search(city=self.city,  date_from='2023-08-07', date_to='2023-07-07')
        self.assertEqual(cities, {})