from rest_framework import serializers
from .models import *
from rest_framework import exceptions


class USerializer(serializers.ModelSerializer):
    class Meta:
        model = U
        fields = "__all__"


class ApplianceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appliances
        fields = "__all__"
        
