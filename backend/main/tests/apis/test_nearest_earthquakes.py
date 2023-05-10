
from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient

from main.tests.factories import CityFactory


class ProjectDetailTestTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.search_url = reverse("main:search")

        self.city = CityFactory(name='Los Angeles, CA', lat=34.052235, lon=-118.243683)

        self.search_data = {
            'date_from': '2021-06-07',
            'date_to': '2021-07-07',
            'city_id': self.city.id,
        }

    def test_search_nearest_earthquakes(self):
        """Test search nearest earthquakes."""
        response = self.client.post(self.search_url, self.search_data)
        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.data['city'], 'Los Angeles, CA')
        self.assertEqual(response.data['date_from'], 'June 07 2021')
        self.assertEqual(response.data['date_to'], 'July 07 2021')
        self.assertEqual(response.data['closest_earthquake'], 'Corral del Risco (Punta de Mita), Mexico')
        self.assertEqual(response.data['magnitude'], 5.6 )
        self.assertEqual(response.data['date'], 'July 04')
    
    def test_search_nearest_earthquakes_empty(self):
        """Test search nearest earthquakes empty."""
        self.search_data['date_from'] = '2021-07-07'
        self.search_data['date_to'] = '2021-07-07'
        response = self.client.post(self.search_url, self.search_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {})

    def test_search_nearest_earthquakes_empty_date_from(self):
        """Test search nearest earthquakes empty date_from."""
        self.search_data['date_from'] = ''
        response = self.client.post(self.search_url, self.search_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["extra"]["fields"]['date_from'][0], 'Date has wrong format. Use one of these formats instead: YYYY-MM-DD.')
    
    def test_search_nearest_earthquakes_empty_date_to(self):
        """Test search nearest earthquakes empty date_to."""
        self.search_data['date_to'] = ''
        response = self.client.post(self.search_url, self.search_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["extra"]["fields"]['date_to'][0], 'Date has wrong format. Use one of these formats instead: YYYY-MM-DD.')
    
    def test_search_nearest_earthquakes_empty_city_id(self):
        """Test search nearest earthquakes empty city_id."""
        self.search_data['city_id'] = ''
        response = self.client.post(self.search_url, self.search_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["extra"]["fields"]['city_id'][0], 'A valid integer is required.')
    
    def test_search_nearest_earthquakes_empty_data(self):
        """Test search nearest earthquakes empty data."""
        self.search_data['date_from'] = ''
        self.search_data['date_to'] = ''
        self.search_data['city_id'] = ''
        response = self.client.post(self.search_url, self.search_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["extra"]["fields"]['date_from'][0], 'Date has wrong format. Use one of these formats instead: YYYY-MM-DD.')
        self.assertEqual(response.data["extra"]["fields"]['date_to'][0], 'Date has wrong format. Use one of these formats instead: YYYY-MM-DD.')
        self.assertEqual(response.data["extra"]["fields"]['city_id'][0], 'A valid integer is required.')
    
    def test_search_nearest_earthquakes_invalid_date_from(self):
        """Test search nearest earthquakes invalid date_from."""
        self.search_data['date_from'] = '2021-07-07 00:00:00'
        response = self.client.post(self.search_url, self.search_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["extra"]["fields"]['date_from'][0], 'Date has wrong format. Use one of these formats instead: YYYY-MM-DD.')

    def test_search_nearest_earthquakes_invalid_date_to(self):
        """Test search nearest earthquakes invalid date_to."""
        self.search_data['date_to'] = '2021-07-07 00:00:00'
        response = self.client.post(self.search_url, self.search_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["extra"]["fields"]['date_to'][0], 'Date has wrong format. Use one of these formats instead: YYYY-MM-DD.')

    def test_search_nearest_earthquakes_invalid_city_id(self):
        """Test search nearest earthquakes invalid city_id."""
        self.search_data['city_id'] = '1.1'
        response = self.client.post(self.search_url, self.search_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["extra"]["fields"]['city_id'][0], 'A valid integer is required.')

    def test_search_nearest_earthquakes_city_does_not_exist(self):
        """Test search nearest earthquakes city does not exist."""
        self.search_data['city_id'] = 100
        response = self.client.post(self.search_url, self.search_data)
        self.assertEqual(response.status_code, 404)

    def test_search_nearest_earthquakes_datefrom_greater_dateto(self):
        """Test search nearest earthquakes datefrom greater dateto."""
        self.search_data['date_from'] = '2021-07-08'
        self.search_data['date_to'] = '2021-07-07'
        response = self.client.post(self.search_url, self.search_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["extra"]["fields"]['non_field_errors'][0], 'date_to must be greater than date_from')
    
    def test_search_nearest_earthquakes_datefrom_greater_today(self):
        """Test search nearest earthquakes datefrom greater today."""
        self.search_data['date_from'] = '2100-07-09'
        self.search_data['date_to'] = '2200-07-07'
        response = self.client.post(self.search_url, self.search_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["extra"]["fields"]['non_field_errors'][0], 'date_to cannot be greater than today')
