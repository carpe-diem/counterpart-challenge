
from datetime import date

from main.models import City, SearchHistory
from main.exceptions import ApplicationError


def search_create(*, 
                    city: City,
                    date_from: date,
                    date_to: date,
                    closest_earthquake: str,
                    magnitude: float,
                    date: date) -> dict:

    search = SearchHistory(
        city=city,
        date_from=date_from,
        date_to=date_to,
        closest_earthquake=closest_earthquake,
        magnitude=magnitude,
        date=date
        )

    search.full_clean()
    search.save()

    return search