from django.urls import include, path
from rest_framework import routers
from . import views
from collegeapp.controllers import major_controller


router = routers.DefaultRouter()
router.register(r"subjects", views.SubjectViewSet)
router.register(r"students", views.StudentViewSet)
router.register(r"studentapplications", views.StudentApplicationViewSet)
router.register(r"administrators", views.AdministratorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login', views.AppLogin.as_view()),
    path('token/refresh', views.TokenRefresh.as_view()),
    path('token/validate', views.TokenValidate.as_view()),
    path('user/validate', views.UserValidate.as_view()),
    path('majors', major_controller.ListMajors.as_view()),
    path('major/<int:id>/subjects', major_controller.ListSubjectsOfMajor.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]