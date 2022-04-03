from django.http import HttpResponse, JsonResponse
from .models import IpPools
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import IpSerializer
from rest_framework.response import Response
from apps.account.utils.auth import UserAuthentication


# Create your views here.


# def GetIp(request):
#     querySet = IpPools.objects.all()
#     lst = []
#     dic, result = {}, {}
#     for r in querySet:
#         dic['ip'] = r.ip
#         dic['status'] = r.status
#         lst.append(dic)
#     result['result'] = lst
#     return JsonResponse(result)

class IpsView(APIView):
    authentication_classes = [UserAuthentication, ]

    def get(self, request):
        ip = IpPools.objects.filter(speed__lt=0, disable_domains__nin='ti.com').first()
        serializer = IpSerializer(instance=ip)
        return Response(serializer.data)
