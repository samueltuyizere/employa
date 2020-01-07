from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    model = EmployeeSerializer
    fields = all