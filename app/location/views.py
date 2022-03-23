from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Location
from .serializers import LocationSerializer
from rest_framework import filters
from rest_framework.response import Response
class LocationView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Location.objects.all()
    serializer_class=LocationSerializer
