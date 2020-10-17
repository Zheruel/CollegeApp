from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r"colleges", views.CollegeViewSet)
router.register(r"majors", views.MajorViewSet)
router.register(r"subjects", views.SubjectViewSet)
router.register(r"students", views.StudentViewSet)
router.register(r"studentapplications", views.StudentApplicationViewSet)
router.register(r"administrators", views.AdministratorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login', views.AppLogin.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]