from django.core.exceptions import ValidationError
from django.test import TestCase

from main.services.city_create import city_create


class CityCreateTests(TestCase):

    def test_city_create(self):
        data = {
            'name': 'Los Angeles, CA',
            'lat': 34.052235,
            'lon': -118.243683,
        }
        city = city_create(**data)
        self.assertEqual(city.name, data['name'])
        self.assertEqual(city.lat, data['lat'])
        self.assertEqual(city.lon, data['lon'])

    def test_city_create_empty_name(self):
        """Test city_create service empty name."""
        data = {
            'name': '',
            'lat': 34.052235,
            'lon': -118.243683,
        }
        with self.assertRaises(ValidationError):
            city_create(**data)

    def test_city_create_empty_lat(self):
        """Test city_create service empty lat."""
        data = {
            'name': 'Los Angeles, CA',
            'lat': '',
            'lon': -118.243683,
        }
        with self.assertRaises(ValidationError):
            city_create(**data)
    
    def test_city_create_empty_lon(self):
        """Test city_create service empty lon."""
        data = {
            'name': 'Los Angeles, CA',
            'lat': 34.052235,
            'lon': '',
        }
        with self.assertRaises(ValidationError):
            city_create(**data)
    
    def test_city_create_empty_data(self):
        """Test city_create service empty data."""
        data = {
            'name': '',
            'lat': '',
            'lon': '',
        }
        with self.assertRaises(ValidationError):
            city_create(**data)
    
    def test_city_create_invalid_lat(self):
        """Test city_create service invalid lat."""
        data = {
            'name': 'Los Angeles, CA',
            'lat': 'invalid',
            'lon': -118.243683,
        }
        with self.assertRaises(ValidationError):
            city_create(**data)

    def test_city_create_invalid_lon(self):
        """Test city_create service invalsid lon."""
        data = {
            'name': 'Los Angeles, CA',
            'lat': 34.052235,
            'lon': 'invalid',
        }
        with self.assertRaises(ValidationError):
            city_create(**data)
    
    def test_city_create_invalid_data(self):
        """Test city_create service invalid data."""
        data = {
            'name': 'Los Angeles, CA',
            'lat': 'invalid',
            'lon': 'invalid',
        }
        with self.assertRaises(ValidationError):
            city_create(**data)
    
    def test_city_create_duplicate(self):
        """Test city_create service duplicate."""
        data = {
            'name': 'Los Angeles, CA',
            'lat': 34.052235,
            'lon': -118.243683,
        }
        city_create(**data)
        with self.assertRaises(ValidationError):
            city_create(**data)

    def test_city_create_duplicate_name(self):
        """Test city_create service duplicate name."""
        data = {
            'name': 'Los Angeles, CA',
            'lat': 34.052235,
            'lon': -118.243683,
        }
        city_create(**data)
        data['lat'] = 34.052236
        with self.assertRaises(ValidationError):
            city_create(**data)

    def test_city_create_duplicate_lat_lon(self):

        """Test city_create service duplicate lat."""
        data = {
            'name': 'Los Angeles, CA',
            'lat': 34.052235,
            'lon': -118.243683,
        }
        city_create(**data)
        data['name'] = 'Los Angeles, CA 2'
        with self.assertRaises(ValidationError):
            city_create(**data)

