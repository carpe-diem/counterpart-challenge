from django.urls import path

from main.apis.cities_list import CitiesListApi
from main.apis.city_create import CitiesCreateApi
from main.apis.nearest_earthquakes import NearestEarthquakesSearchApi


app_name = 'main'


urlpatterns = [
    path('cities', CitiesListApi.as_view(), name='list'),
    path('cities/create', CitiesCreateApi.as_view(), name='create'),
    path('search', NearestEarthquakesSearchApi.as_view(), name='search'),
]