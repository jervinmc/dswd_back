from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Cases
from .serializers import CasesSerializer
from rest_framework import permissions
from rest_framework import filters
from rest_framework.response import Response
class CasesView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    permission_classes=[permissions.AllowAny]
    search_fields = ['category','price','name','descriptions']
    queryset=Cases.objects.all()
    serializer_class=CasesSerializer
