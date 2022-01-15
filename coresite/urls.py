from rest_framework import routers
from django.urls import include, path
from . import views

router = routers.DefaultRouter()
router.register(r'students', views.StudentViewsets)
router.register('students/id', views.StudentViewsets)
router.register(r'school', views.SchoolViewsets)
router.register(r'school/id', views.SchoolViewsets)
urlpatterns = [
    path('', include(router.urls)),
    path('', include('rest_framework.urls', namespace='rest_framework'))

]
