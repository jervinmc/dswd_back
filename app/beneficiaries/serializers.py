from rest_framework import serializers
from .models import Beneficiaries

class BeneficiariesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Beneficiaries
        fields="__all__"
