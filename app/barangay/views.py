from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Barangay
from .serializers import BarangaySerializer
from rest_framework import filters
from rest_framework.response import Response
class BarangayView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    # search_fields = ['category','price','name','descriptions']
    queryset=Barangay.objects.all()
    serializer_class=BarangaySerializer


