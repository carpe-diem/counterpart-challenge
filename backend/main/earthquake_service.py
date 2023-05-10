from datetime import date

from django.core.cache import cache

from geopy.distance import distance
import numpy as np
import requests


# TODO - move to .env
EARTHQUAKE_URL = 'https://earthquake.usgs.gov/fdsnws/event/1/query.geojson'


# TODO Test
class EarthquakeApiClient():

    def __init__(self, lat: float, lon: float, date_from: date, date_to: date, magnitude: float=5) -> None:
        self.lat = lat
        self.lon = lon
        self.magnitude = magnitude
        self.date_from = date_from
        self.date_to = date_to

    def _payload(self):
        return {
            'format': 'geojson',
            'orderby':'time',
            'starttime': self.date_from,
            'endtime': self.date_to,
            'minmagnitude': self.magnitude,            
        }

    def _format_city(self, response):
        city = response['properties']['place'].split(' of ')[-1]
        response['properties']['place'] = city
        return response
    
    def _get_closest_earthquake(self, response):
        coords = np.array([(f['geometry']['coordinates'][1], f['geometry']['coordinates'][0]) for f in response])
        dists = np.array([distance((self.lat, self.lon), c).km for c in coords])
        idx = np.argmin(dists)

        return self._format_city(response[idx])

    def _get_earthquakes(self):
        cache_key = f"earthquake_api_response_{self.lat}_{self.lon}_{self.date_from}_{self.date_to}"
        data = cache.get(cache_key)

        if data is None:
            # Si no hay datos en caché, haz la solicitud a la API
            response = requests.get(EARTHQUAKE_URL, params=self._payload())
            data = response.json()

            cache.set(cache_key, data)

        return data

    def get_nearest_earthquake(self):
        data = self._get_earthquakes()

        if data['metadata']['count'] == 0:
            return {}
        
        return self._get_closest_earthquake(data['features'])

