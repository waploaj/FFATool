from .models import Employee
from rest_framework import serializers

class Employeeserialixer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'username','person'
        )