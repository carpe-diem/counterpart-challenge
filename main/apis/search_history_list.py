# -*- coding: utf-8 -*-
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from main.selectors.search_history_list import search_history_list


class SearchHistoryListApi(APIView):

    class OutputSerializer(serializers.Serializer):
        city = serializers.CharField()
        date_from = serializers.DateField()
        date_to = serializers.DateField()
        closest_earthquake = serializers.CharField()
        magnitude = serializers.FloatField()
        date = serializers.DateField()
        created = serializers.DateTimeField()

    def get(self, request):
        searches = search_history_list()

        data = self.OutputSerializer(searches, many=True).data

        return Response(data)