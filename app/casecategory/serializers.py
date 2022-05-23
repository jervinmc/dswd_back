from rest_framework import serializers
from .models import CaseCategory

class CaseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=CaseCategory
        fields="__all__"
