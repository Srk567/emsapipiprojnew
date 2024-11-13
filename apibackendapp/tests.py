from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from .models import Department, Employee
from datetime import date
from django.urls import reverse
from rest_framework import status
from .serializers import EmployeeSerializer


class EmployeeViewSetTest(APITestCase):
    def setUp(self):
        self.department = Department.objects.create(DepartmentName='HR')
        self.employee = Employee.objects.create(
            EmployeeName="jackchan",
            Designation="master",
            DateofJoining=date(2024, 11, 13),
            DepartmentId=self.department,
            Contact="China",
            IsActive=True
        )
        self.client = APIClient()

    def test_employee_detail(self):
        # Update to use list for args, and verify URL name
        url = reverse('Employee-details', args={self.employee.EmployeeId})
        
        response = self.client.get(url)
        employees = Employee.objects.all()
        
        # Fetch the employee and serialize it
        serializer = EmployeeSerializer(self.employee)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
