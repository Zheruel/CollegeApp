from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CollegeSerializer, MajorSerializer, SubjectSerializer, StudentSerializer, StudentApplicationSerializer, AdministratorSerializer
from .models import College, Major, Subject, Student, StudentApplication, Administrator

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