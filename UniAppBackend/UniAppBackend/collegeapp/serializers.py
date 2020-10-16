from rest_framework import serializers
from .models import College, Major, Subject, Student, StudentApplication, Administrator


class CollegeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = College
        fields = ("id", "name")

class MajorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Major
        fields = ("id", "name", "quota", "college")

class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = ("id", "name", "major")

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ("id", "firstName", "lastName", "email", "password")

class StudentApplicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StudentApplication
        fields = ("id", "birthDate", "birthPlace", "highSchoolName", "coverLetter", "highSchoolDocument", "highSchoolGPA", "maturaGrade", "student", "major")

class AdministratorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Administrator
        fields = ("id", "email", "password")