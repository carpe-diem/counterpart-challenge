import factory
import factory.fuzzy

from main.models import City, SearchHistory



class CityFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: f'Test City Name {n}')
    lat = factory.fuzzy.FuzzyFloat(-90.0, 90.0)
    lon = factory.fuzzy.FuzzyFloat(-90.0, 90.0)

    class Meta:
        model = City

class SearchHistoryFactory(factory.django.DjangoModelFactory):
    city = factory.SubFactory(CityFactory)
    date_from = factory.fuzzy.FuzzyDate()
    date_to = factory.fuzzy.FuzzyDate()
    closest_earthquake = factory.Sequence(lambda n: f'Test Closest Earthquake {n}')
    magnitude = factory.fuzzy.FuzzyFloat(0.0, 10.0)
    date = factory.fuzzy.FuzzyDate()

    class Meta:
        model = SearchHistory
