from typing import Iterable

from main.models import City


def cities_list() -> Iterable[City]:
    cities = City.objects.all().order_by('name')
    return cities