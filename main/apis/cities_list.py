# -*- coding: utf-8 -*-
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from main.selectors.cities_list import cities_list

class CitiesListApi(APIView):

    class OutputSerializer(serializers.Serializer):
        name = serializers.CharField()
        lat = serializers.FloatField()
        lon = serializers.FloatField()

    def get(self, request):
        cities = cities_list()

        data = self.OutputSerializer(cities, many=True).data

        return Response(data)