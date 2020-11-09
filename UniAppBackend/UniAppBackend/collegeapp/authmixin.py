from collegeapp import jwtmanager
from django.http import HttpResponseNotFound


class CheckAuth:
    def dispatch(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')

        if token and jwtmanager.verifyToken(token):
            return super().dispatch(request, *args, **kwargs)

        else:
            return HttpResponseNotFound("Auth failed")
