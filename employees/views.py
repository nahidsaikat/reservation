from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from employees.models import Employee
from employees.serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing employees.
    """
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    # permission_classes = [IsAuthenticated]
