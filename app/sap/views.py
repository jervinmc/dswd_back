from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import SAP
from .serializers import SAPSerializer
from rest_framework import permissions
from beneficiaries.models import Beneficiaries
from beneficiaries.serializers import BeneficiariesSerializer
from ps.models import PS
from ps.serializers import PSSerializer
from rest_framework import filters
from rest_framework.response import Response
class SAPView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    permission_classes=[permissions.AllowAny]
    search_fields = ['category','price','name','descriptions']
    queryset=SAP.objects.all()
    serializer_class=SAPSerializer
    # def create(self,request):
    #     data = request.data
    #     # print(self.request.user.id)
    #     # data.user_id=self.request.user.id
    #     serializer = SAPSerializer(data=data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response()


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
        print(request.data.get('barangay'))
        serializer = SAPSerializer(items,many=True)
        print(serializer.data)
        # serializer.is_valid(raise_exception=True)
        return Response(data=serializer.data)


class Requests(generics.GenericAPIView):
    def get(self,request):
        items_beneficiaries = Beneficiaries.objects.filter(status='Pending')
        items_4ps = PS.objects.filter(status='Pending')
        items_sap = SAP.objects.filter(status='Pending')
        sap_serializer = SAPSerializer(items_sap,many=True)
        beneficiaries_serializer = SAPSerializer(items_beneficiaries,many=True)
        ps_serializer = SAPSerializer(items_4ps,many=True)
        listitem = []
        for x in sap_serializer.data:
            listitem.append({"firstname":x['firstname'],"lastname":x['lastname'],"id":x['id'],"request_type":"sap","date_start":x['date_start'],"gender":x['gender'],"address":x['address'],"occupation":x['occupation'],"monthly_salary":x['monthly_salary'],"type_of_id":x['type_of_id'],"id_number":x['id_number'],"cellphone":x['cellphone'],"workplace":x['workplace'],"sector":x['sector'],"barangay":x['barangay'],"status":x['status'],"health_condition":x['health_condition'],"family_member":x['family_member'],"user_id":x['user_id'],"date_start":x['date_start'],"mop":x['mop']})
        for x in beneficiaries_serializer.data:
            listitem.append({"firstname":x['firstname'],"lastname":x['lastname'],"id":x['id'],"request_type":"beneficiaries","date_start":x['date_start']})
        for x in ps_serializer.data:
            listitem.append({"firstname":x['firstname'],"lastname":x['lastname'],"id":x['id'],"request_type":"4ps","date_start":x['date_start']})

        # serializer.is_valid(raise_exception=True)
        return Response(data=listitem)


class CheckSAP(generics.GenericAPIView):
    def get(self,request,user_id=None):
        print("test")
        print(user_id)
        items = SAP.objects.filter(status='Approved',user_id=user_id).count()
        print(items)
        if(items>0):
            return Response(data=True)
        else:
            return Response(data=False)