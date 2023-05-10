# -*- coding: utf-8 -*-
from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from main.services.city_create import city_create


class CitiesCreateApi(APIView):

    class InputSerializer(serializers.Serializer):
        name = serializers.CharField()
        lat = serializers.FloatField()
        lon = serializers.FloatField()

    def post(self, request, *args, **kwargs):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        city_create(**serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED)
