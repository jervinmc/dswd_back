from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Donate
from .serializers import DonateSerializer
from rest_framework import filters
from rest_framework.response import Response
class DonateView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Donate.objects.all()
    serializer_class=DonateSerializer
