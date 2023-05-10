from typing import Iterable

from main.earthquake_service import EarthquakeApiClient
from main.models import City, SearchHistory
from main.services.search_create import search_create
from main.utils import format_date_from_timestamp, format_date_from_string


def search(*, city: City, date_from: str, date_to: str) -> dict:
    """Search for the nearest earthquake for a given city and date range."""
    earthquake = EarthquakeApiClient(
        lat=city.lat,
        lon=city.lon,
        date_from=date_from,
        date_to=date_to
    )

    result = earthquake.get_nearest_earthquake()
    
    if not result:
        return {}

    data = {
        'date_from': format_date_from_string(date_from),
        'date_to': format_date_from_string(date_to),
        'closest_earthquake': result['properties']['place'],
        'magnitude': result['properties']['mag'],
        'date': format_date_from_timestamp(result['properties']['time'])
    }
    
    # TODO This could be stored asynchronously. For example using a celery task.
    search_create(**data, city=city)
    data['city'] = city.name

    return data