from django.test import TestCase
from django.db.models.query import QuerySet

from main.exceptions import ApplicationError
from main.selectors.search import search
from main.tests.factories import CityFactory


class SelectorCitiesListTests(TestCase):
    """Test for cities list selector."""
    def setUp(self):
        self.city = CityFactory(name='Los Angeles, CA', lat=34.052235, lon=-118.243683)

    def test_search(self):
        cities = search(city=self.city,  date_from='2021-06-07', date_to='2021-07-07')
        self.assertIsInstance(cities, dict)
        self.assertEqual(cities['city'], 'Los Angeles, CA')
        self.assertEqual(cities['date_from'], 'June 07 2021')
        self.assertEqual(cities['date_to'], 'July 07 2021')
        self.assertEqual(cities['closest_earthquake'], '101 km S of Merizo Village, Guam')
        self.assertEqual(cities['magnitude'], 5)
        self.assertEqual(cities['date'], 'July 06')
    
    def test_search_empty(self):
        cities = search(city=self.city,  date_from='2023-07-07', date_to='2023-07-07')
        self.assertEqual(cities, {})