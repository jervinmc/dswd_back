from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import PS
from .serializers import PSSerializer
from rest_framework import filters
from rest_framework.response import Response

class PSView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    # search_fields = ['category','price','name','descriptions']
    queryset=PS.objects.all()
    serializer_class=PSSerializer
    # def create(self,request):
    #     data = request.data
    #     # print(self.request.user.id)
    #     # data.user_id=self.request.user.id
    #     serializer = PSSerializer(data={"lastname":data.get('lastname'),"remarks":data.get('remarks'),"image":data.get('image'),"middlename":data.get('middlename'),"status":data.get("status"),"date_start":data.get("date_start"),"firstname":data.get('firstname'),"user_id":self.request.user.id})
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response()

class PSID(generics.GenericAPIView):
    def get(self,request):
        print("test")
        items = PS.objects.filter(user_id=self.request.user.id)
        serializer = PSSerializer(items,many=True)
        # serializer.is_valid(raise_exception=True)
        return Response(data=serializer.data)

class CheckPS(generics.GenericAPIView):
    def get(self,request,user_id=None):
        print("test")
        items = PS.objects.filter(status='Approved',user_id=user_id).count()
        print(user_id)
        print(items)
        if(items>0):
            return Response(data=True)
            
        else:
            return Response(data=False)

