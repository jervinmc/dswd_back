from rest_framework import serializers
from .models import Donate

class DonateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Donate
        fields="__all__"
