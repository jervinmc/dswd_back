from rest_framework import serializers
from .models import PS

class PSSerializer(serializers.ModelSerializer):
    class Meta:
        model=PS
        fields="__all__"
