from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Referral
from .serializers import ReferralSerializer
from rest_framework import filters
from rest_framework.response import Response
class ReferralView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    # search_fields = ['category','price','name','descriptions']
    queryset=Referral.objects.all()
    serializer_class=ReferralSerializer


