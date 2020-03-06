from .models import OsposEmployees
from rest_framework import serializers

class Employeeserialixer(serializers.ModelSerializer):
    class Meta:
        model = OsposEmployees
        fields = (
            'username','person'
        )