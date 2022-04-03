# from abc import ABC

from rest_framework_mongoengine import serializers
from .models import IpPools


# class IpSerializer(serializers.DocumentSerializer):
#     ip = serializers.CharField()
#     status = serializers.CharField()

class IpSerializer(serializers.DocumentSerializer):
    class Meta:
        model = IpPools
        fields = '__all__'
