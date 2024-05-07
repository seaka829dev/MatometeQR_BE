from rest_framework import serializers
from django_filters import rest_framework as filters
from .models import QRInfo

class Serializer(serializers.ModelSerializer):
    class Meta:
        model = QRInfo
        fields = '__all__'
