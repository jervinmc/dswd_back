from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Intervention
from .serializers import InterventionSerializer
from rest_framework import filters
from rest_framework.response import Response
class InterventionView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    # search_fields = ['category','price','name','descriptions']
    queryset=Intervention.objects.all()
    serializer_class=InterventionSerializer


