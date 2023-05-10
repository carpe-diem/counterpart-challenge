from django.test import TestCase
from django.db.models.query import QuerySet

from main.tests.factories import CityFactory

from main.selectors.search_history_list import search_history_list
from main.selectors.search import search
from main.utils import format_date_from_string

class SelectorHistorySearchListTests(TestCase):
    """Test for cities list selector."""
    def setUp(self):
        self.city = CityFactory(name="Test City Name")

    def test_history_search_list(self):
        """Test history search list selector."""
        search(city=self.city,  date_from='2021-06-07', date_to='2021-07-07')
        search(city=self.city,  date_from='2021-06-07', date_to='2021-07-07')

        searches = search_history_list()
        self.assertIsInstance(searches, QuerySet)
        self.assertEqual(len(searches), 2)
        self.assertEqual(searches[0].city.name, 'Test City Name')
        self.assertEqual(searches[0].date_from, format_date_from_string('2021-06-07'))
        self.assertEqual(searches[0].date_to, format_date_from_string('2021-07-07'))
