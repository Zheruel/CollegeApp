from collegeapp.serializers import MajorSerializer, SubjectSerializer
from collegeapp.models import Major, StudentApplication, Subject
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from collegeapp import jwtmanager
from django.utils.decorators import decorator_from_middleware
from collegeapp.authmixin import CheckAuth
from django.core.exceptions import ObjectDoesNotExist


class ListMajors(CheckAuth, APIView):
    def get(self, request):
        queryset = Major.objects.all().order_by("name")

        for major in queryset:
            accepted_applications = StudentApplication.objects.filter(major = major, status=True)
            
            major.quota = "{0}/{1}".format(len(accepted_applications), major.quota)

        serializer = MajorSerializer(queryset, many=True)
          
        return Response(serializer.data)

class ListSubjectsOfMajor(CheckAuth, APIView):
    def get(self, request, id = None):
        try:
            major_check = Major.objects.get(pk = id)

            queryset = Subject.objects.filter(major = id)
            serializer = SubjectSerializer(queryset, many=True)
          
            return Response(serializer.data)

        except ObjectDoesNotExist:
            return Response("No such major", status=status.HTTP_400_BAD_REQUEST)

          