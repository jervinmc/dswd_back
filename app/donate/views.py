from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Donate
from .serializers import DonateSerializer
from rest_framework import filters
from rest_framework.response import Response

class DonateView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    # search_fields = ['category','price','name','descriptions']
    queryset=Donate.objects.all()
    serializer_class=DonateSerializer
    # def create(self,request):
    #     data = request.data
    #     # print(self.request.user.id)
    #     # data.user_id=self.request.user.id
    #     serializer = DonateSerializer(data={"lastname":data.get('lastname'),"remarks":data.get('remarks'),"image":data.get('image'),"middlename":data.get('middlename'),"status":data.get("status"),"category":data.get("category"),"date_start":data.get("date_start"),"firstname":data.get('firstname'),"user_id":self.request.user.id})
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response()

class DonateID(generics.GenericAPIView):
    def get(self,request):
        print("test")
        items = Donate.objects.filter(user_id=self.request.user.id)
        serializer = DonateSerializer(items,many=True)
        # serializer.is_valid(raise_exception=True)
        return Response(data=serializer.data)


