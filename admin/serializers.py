from rest_framework import serializers
from . import models


class AdminLogin(serializers.Serializer):
    username = serializers.CharField(max_length=64)
    password = serializers.CharField(max_length=64)


class AdminSignUp(serializers.ModelSerializer):
    class Meta:
        model = models.Employe
        fields = '__all__'
