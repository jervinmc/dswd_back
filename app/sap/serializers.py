from rest_framework import serializers
from .models import SAP

class SAPSerializer(serializers.ModelSerializer):
    class Meta:
        model=SAP
        fields="__all__"
