from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http.request import HttpRequest
# from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import  BasicAuthentication
from .models import (
    MacAddress
) 
from .serializers import (
    MacAddressSerializer
)

@api_view(["POST"])
def check_mac_address_is_exist(request:HttpRequest,mac_address:str):
    # print(request.META)
    try :
        mac_object = MacAddress.objects.get(mac_address=mac_address)
    except ObjectDoesNotExist :
        mac_object = None

    return Response(
        {
            "isExist": isinstance(mac_object,MacAddress) ,
            "data": MacAddressSerializer(mac_object).data if  isinstance(mac_object,MacAddress) else None,
        } ,
    )

@api_view(["POST"])
def check_mac_address_exist(request:HttpRequest):
    print(request.body)
    try :
        mac_object = MacAddress.objects.get(mac_address=request.body['mac_address'])
    except ObjectDoesNotExist :
        mac_object = None

    return Response(
        {
            "isExist": isinstance(mac_object,MacAddress) ,
            "data": MacAddressSerializer(mac_object).data if  isinstance(mac_object,MacAddress) else None,
        } ,
    )

class MacAddressesListAPIView(ListAPIView):
    queryset = MacAddress.objects.all()
    serializer_class = MacAddressSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated] 

