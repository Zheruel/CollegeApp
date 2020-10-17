from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from . import jwtmanager

class CollegeViewSet(viewsets.ModelViewSet):
    queryset = College.objects.all().order_by("name")
    serializer_class = CollegeSerializer

class MajorViewSet(viewsets.ModelViewSet):
    queryset = Major.objects.all().order_by("name")
    serializer_class = MajorSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all().order_by("name")
    serializer_class = SubjectSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by("firstName")
    serializer_class = StudentSerializer

class StudentApplicationViewSet(viewsets.ModelViewSet):
    queryset = StudentApplication.objects.all().order_by("id")
    serializer_class = StudentApplicationSerializer

class AdministratorViewSet(viewsets.ModelViewSet):
    queryset = Administrator.objects.all().order_by("email")
    serializer_class = AdministratorSerializer

class AppLogin(APIView):
    def post(self, request, format=None):
        serializer = LoginSerializer(data = request.data)

        if serializer.is_valid():
            encoded_jwt = jwtmanager.getToken(serializer.data, "user")
            test = jwtmanager.verifyToken(encoded_jwt)
            encoded_jwt2 = jwtmanager.refreshToken(encoded_jwt)

            return Response(encoded_jwt2, status = status.HTTP_200_OK)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)