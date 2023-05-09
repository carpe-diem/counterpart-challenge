from typing import Iterable

from main.earthquake_service import EarthquakeApiClient
from main.models import City
from main.utils import format_date, format_timestamp


def search(*, city: City, date_from: str, date_to: str) -> dict:
    """Search for the nearest earthquake for a given city and date range."""
    earthquake = EarthquakeApiClient(
        lat=city.lat,
        lon=city.lon,
        date_from=date_from,
        date_to=date_to
    )

    result = earthquake.get_nearest_earthquake()
    # TODO save search to database
    import pdb; pdb.set_trace()
    
    if not result:
        return {}

    result = result[0]
    data = {
        'city': city.name,
        'date_from': format_date(date_from),
        'date_to': format_date(date_to),
        'closest_earthquake': result['properties']['place'],
        'magnitude': result['properties']['mag'],
        'date': format_timestamp(result['properties']['time'], year=False)
    }
    return data