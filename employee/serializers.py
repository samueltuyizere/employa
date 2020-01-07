from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ('url', 'first_name', 'last_name', 'phone_number', 'national_id', 'email', 'date_of_birth', 'status', 'postion')