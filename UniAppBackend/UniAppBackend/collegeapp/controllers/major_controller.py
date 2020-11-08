from django.shortcuts import render
from collegeapp.serializers import MajorSerializer
from collegeapp.models import Major
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from collegeapp import jwtmanager
from django.utils.decorators import decorator_from_middleware
from django.http import HttpResponseNotFound
from collegeapp.authmixin import CheckAuth


class ListMajors(CheckAuth, APIView):
    queryset = Major.objects.all().order_by("name")
    serializer_class = MajorSerializer

    def get(self, request):
        queryset = Major.objects.all().order_by("name")
        serializer = MajorSerializer(queryset, many=True)

        return Response(serializer.data)