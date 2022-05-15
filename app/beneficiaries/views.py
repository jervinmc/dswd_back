from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Beneficiaries
from .serializers import BeneficiariesSerializer
from rest_framework import filters
from rest_framework.response import Response
class BeneficiariesView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    # search_fields = ['category','price','name','descriptions']
    queryset=Beneficiaries.objects.all()
    serializer_class=BeneficiariesSerializer
    # def create(self,request):
    #     data = request.data
    #     # print(self.request.user.id)
    #     # data.user_id=self.request.user.id
    #     serializer = BeneficiariesSerializer(data={"location":data.get('location'),"lastname":data.get('lastname'),"middlename":data.get('middlename'),"occupation":data.get('occupation'),"status":data.get("status"),"firstname":data.get('firstname'),"user_id":self.request.user.id,"date_start":data.get('date_start'),"beneficiaries_type":data.get('beneficiaries_type')})
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response()

class BeneficiariesID(generics.GenericAPIView):
    def get(self,request):
        print("test")
        items = Beneficiaries.objects.filter(user_id=self.request.user.id)
        serializer = BeneficiariesSerializer(items,many=True)
        # serializer.is_valid(raise_exception=True)
        return Response(data=serializer.data)