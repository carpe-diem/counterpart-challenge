from datetime import date
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

    def _get_earthquakes(self):
        response = requests.get(EARTHQUAKE_URL, params=self._payload())
        data = response.json()

        # Storre data in cache/db. Maybe use redis?
        return data

    def get_nearest_earthquake(self):
        data = self._get_earthquakes()
        # TODO - get nearest earthquake
        return data['features']

