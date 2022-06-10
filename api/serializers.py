
from rest_framework import serializers
from employe.models import Employe

class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employe
        fields = '__all__'
        