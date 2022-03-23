from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import SAP
from .serializers import SAPSerializer
from rest_framework import permissions
from rest_framework import filters
from rest_framework.response import Response
class SAPView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    permission_classes=[permissions.AllowAny]
    search_fields = ['category','price','name','descriptions']
    queryset=SAP.objects.all()
    serializer_class=SAPSerializer
    def create(self,request):
        data = request.data
        # print(self.request.user.id)
        # data.user_id=self.request.user.id
        serializer = SAPSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response()


class SAPID(generics.GenericAPIView):
    def get(self,request):
        print("test")
        items = SAP.objects.filter(user_id=self.request.user.id)
        serializer = SAPSerializer(items,many=True)
        # serializer.is_valid(raise_exception=True)
        return Response(data=serializer.data)


class SAPBarangay(generics.GenericAPIView):
    def post(self,request):
        items = SAP.objects.filter(barangay=request.data.get('barangay'))
        serializer = SAPSerializer(items,many=True)
        # serializer.is_valid(raise_exception=True)
        return Response(data=serializer.data)