import factory
import factory.fuzzy

from main.models import City



class CityFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: f'Test City Name {n % 5}')
    lat = factory.fuzzy.FuzzyFloat(0.0)
    lon = factory.fuzzy.FuzzyFloat(0.0)

    class Meta:
        model = City
