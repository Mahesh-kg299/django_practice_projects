from rest_framework import serializers
from .models import Employee, Department

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["e_name", "e_gender", "e_dob", "e_salary", "e_email", "e_dprt"]

class DepartmentSerializer(serializers.ModelSerializer):
    employee = serializers.PrimaryKeyRelatedField(read_only = True, many = True)
    # employee = serializers.StringRelatedField(many = True)
    # employee = serializers.SlugRelatedField(read_only = True, many = True, slug_field= "e_name")
    # employee = serializers.HyperlinkedRelatedField(read_only = True, many = True, view_name= "employee-detail")
    class Meta:
        model = Department
        fields = ["dprt_name", "employee"]