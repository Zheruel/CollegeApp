from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from . import jwtmanager
import django.core.exceptions
from django.contrib.auth.hashers import make_password, check_password

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

    def create(self, request):
        serializer = StudentSerializer(data = request.data)

        if serializer.is_valid():
            if Student.objects.filter(email = serializer.data["email"].lower()).exists():
                return Response("Email is already taken", status = status.HTTP_400_BAD_REQUEST)

            else:
                return super().create(request)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

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
            try:
                adminObject = Administrator.objects.get(email=serializer.data["email"])

                if check_password(serializer.data["password"], adminObject.password):
                    encoded_jwt = jwtmanager.getToken(serializer.data, "administrator")

                    return Response(encoded_jwt, status = status.HTTP_200_OK)

                else:
                    return Response("Login information is wong", status = status.HTTP_400_BAD_REQUEST)

            except django.core.exceptions.ObjectDoesNotExist:
                try:
                    studentObject = Student.objects.get(email=serializer.data["email"])

                    if check_password(serializer.data["password"], studentObject.password):
                        encoded_jwt = jwtmanager.getToken(serializer.data, "student")

                        return Response(encoded_jwt, status = status.HTTP_200_OK)

                    else:
                        return Response("Login information is wrong", status = status.HTTP_400_BAD_REQUEST)

                except django.core.exceptions.ObjectDoesNotExist:
                    return Response("Login failed", status = status.HTTP_400_BAD_REQUEST)

        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class TokenRefresh(APIView):
    def post(self, request, format=None):
        serializer = TokenSerializer(data = request.data)

        if serializer.is_valid():
            token = jwtmanager.refreshToken(serializer.data["token"])

            if(token != False):
                encoded_jwt = token

                return Response(encoded_jwt, status = status.HTTP_200_OK)
           
            else:
                return Response("Token is not valid", status = status.HTTP_400_BAD_REQUEST)

        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class TokenValidate(APIView):
    def post(self, request, format=None):
        serializer = TokenSerializer(data = request.data)

        if serializer.is_valid():
            if(jwtmanager.verifyToken(serializer.data["token"])):
                return Response("Token is valid", status = status.HTTP_200_OK)

            else:
                return Response("Token is invalid", status = status.HTTP_400_BAD_REQUEST)
