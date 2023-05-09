from django.shortcuts import get_object_or_404
from django.utils import timezone

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import City
from main.selectors.search import search

class NearestEarthquakesSearchApi(APIView):

    class InputSerializer(serializers.Serializer):
        date_from = serializers.DateField()
        date_to = serializers.DateField()
        city_id = serializers.IntegerField()

        def validate(self, data):
            date_from = data.get('date_from')
            date_to = data.get('date_to')
            if date_to < date_from:
                raise serializers.ValidationError('date_to must be greater than date_from')
            if date_to > timezone.now().date():
                raise serializers.ValidationError('date_to cannot be greater than today')
            return data

    # class OutputSerializer(serializers.Serializer):
    #     city = serializers.CharField()
    #     date_from = serializers.CharField()
    #     date_to = serializers.CharField()
    #     closest_earthquake = serializers.CharField()
    #     magnitude = serializers.FloatField()
    #     date = serializers.CharField()

    def post(self, request, *args, **kwargs):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        city = get_object_or_404(City, id=serializer.validated_data['city_id'])

        result = search(
            city=city,
            date_from=serializer.validated_data['date_from'].strftime('%Y-%m-%d'),
            date_to=serializer.validated_data['date_to'].strftime('%Y-%m-%d')
        )

        return Response(result)