
from main.models import City
from main.exceptions import ApplicationError


def city_create(*, name: str, lat: float, lon: float) -> City:
    city = City(
        name=name,
        lat=lat,
        lon=lon
        )

    city.full_clean()
    city.save()

    return city