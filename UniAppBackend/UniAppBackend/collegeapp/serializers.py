from rest_framework import serializers
from .models import College, Major, Subject, Student, StudentApplication, Administrator
from django.contrib.auth.hashers import make_password


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
    def create(self, validated_data):
        validated_data["email"] = validated_data["email"].lower()
        validated_data["password"] = make_password(validated_data["password"])

        return Student.objects.create(**validated_data)

    class Meta:
        model = Student
        fields = ("id", "firstName", "lastName", "email", "password")

class StudentApplicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StudentApplication
        fields = ("id", "birthDate", "birthPlace", "highSchoolName", "coverLetter", "highSchoolDocument", "highSchoolGPA", "maturaGrade", "student", "major")

class AdministratorSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])

        return Administrator.objects.create(**validated_data)

    class Meta:
        model = Administrator
        fields = ("id", "email", "password")

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required = True)
    password = serializers.CharField(required = True)

    def create(self, validated_data):
        return validated_data

class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(required = True)

    def create(self, validated_data):
        return validated_data