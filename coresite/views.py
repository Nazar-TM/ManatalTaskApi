from rest_framework import permissions
from rest_framework import viewsets
from . models import School, Student
from . serializers import SchoolSerializer, StudentSerializer


# Create your views here.
class SchoolViewsets(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [permissions.IsAuthenticated]


class StudentViewsets(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('id')
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]
