from rest_framework import serializers
from .models import Barangay

class BarangaySerializer(serializers.ModelSerializer):
    class Meta:
        model=Barangay
        fields="__all__"
