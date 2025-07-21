from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Employee, Department
from .serializers import EmployeeSerializer, DepartmentSerializer
from django.http import JsonResponse 

# class Employee_list(APIView):
#     def get(self, request, format = None):
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees, many = True, context= {"request": request})
#         return Response(serializer.data)
    
#     def post(self, request, format = None):
#         serialzer = EmployeeSerializer(data= request.data)
#         if serialzer.is_valid():
#             serialzer.save()
#             return Response(serialzer.data)

# class Department_list(APIView):
#     def get(self, request, format = None):
#         departments = Department.objects.all()
#         serializer = DepartmentSerializer(departments, many = True)
#         return Response(serializer.data)
    
#     def post(self, request, format = None):
#         serialzer = DepartmentSerializer(data= request.data)
#         if serialzer.is_valid():
#             serialzer.save()
#             return Response(serialzer.data)

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer