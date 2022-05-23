from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import CaseCategory
from .serializers import CaseCategorySerializer
from rest_framework import filters
from rest_framework.response import Response
from intervention.models import Intervention
from intervention.serializers import InterventionSerializer
from referral.models import Referral
from referral.serializers import ReferralSerializer
class CaseCategoryView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    # search_fields = ['category','price','name','descriptions']
    queryset=CaseCategory.objects.all()
    serializer_class=CaseCategorySerializer



class CaseCategoryBulk(generics.GenericAPIView):
    def post(self,request):
        res = request.data
        CaseCategory.objects.filter(case_id = res.get('case_id')).delete()
        Intervention.objects.filter(case_id = res.get('case_id')).delete()
        Referral.objects.filter(case_id = res.get('case_id')).delete()
        for x in res.get('cases'):
            serializer =  CaseCategorySerializer(data ={"case_id":res.get('case_id'),"name":x})
            serializer.is_valid(raise_exception=True)
            serializer.save()

        for x in res.get('intervention'):
            serializer =  InterventionSerializer(data ={"case_id":res.get('case_id'),"name":x})
            serializer.is_valid(raise_exception=True)
            serializer.save()
        
        for x in res.get('referral'):
            serializer =  ReferralSerializer(data ={"case_id":res.get('case_id'),"name":x})
            serializer.is_valid(raise_exception=True)
            serializer.save()

        return Response(data=serializer.data)

class CaseCategoryCaseID(generics.GenericAPIView):
    def get(self,request,case_id=None):
        listitem_case = []
        items = CaseCategory.objects.filter(case_id = case_id)
        items = CaseCategorySerializer(items,many=True)
        for x in items.data:
            listitem_case.append(x['name'])

        listitem_intervention = []
        items = Intervention.objects.filter(case_id = case_id)
        items = InterventionSerializer(items,many=True)
        for x in items.data:
            listitem_intervention.append(x['name'])
        

        listitem_referral = []
        items = Referral.objects.filter(case_id = case_id)
        items = ReferralSerializer(items,many=True)
        for x in items.data:
            listitem_referral.append(x['name'])
        return Response(data={"cases":listitem_case,"intervention":listitem_intervention,"referral":listitem_referral})