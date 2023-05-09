from django.urls import path

from main.apis.cities_list import CitiesListApi


app_name = 'main'


urlpatterns = [
    path('cities', CitiesListApi.as_view(), name='list'),

]