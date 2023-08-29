from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
# from django.http.request import HttpRequest
# from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.request import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import  BasicAuthentication
from .models import (
    MacAddress ,
    TelegramBot ,
    ChatInfo ,
) 
from .serializers import (
    MacAddressSerializer ,
    TelegramBotSerializer ,
    ChatInfoSerializer ,
)



@api_view(["GET"])
def check_mac_address_is_exist(request:HttpRequest,mac_address:str):
    try :
        mac_object = MacAddress.objects.get(mac_address=mac_address)
    except ObjectDoesNotExist :
        mac_object = None
    return Response(
        {
            "success" : True ,
            "response":{
                "isExist": isinstance(mac_object,MacAddress) ,
                "data": MacAddressSerializer(mac_object).data if  isinstance(mac_object,MacAddress) else None,
            },
        },
        )


@api_view(["POST"])
def check_mac_address_exist(request:HttpRequest):
    if request.data == {} or 'mac_address' not in request.data.keys() :
        return Response(
            {  
                "success": False ,
                "response":"Please Attach mac_address in raw data as json" ,
            }
        )
    else :
        try :
            mac_object = MacAddress.objects.get(mac_address=request.data.get('mac_address'))
        except Exception as e :
            print(e)
            mac_object = None
        return Response(
        {
            "success" : True ,
            "response":{
                "isExist": isinstance(mac_object,MacAddress) ,
                "data": MacAddressSerializer(mac_object).data if  isinstance(mac_object,MacAddress) else None,
            },
        },
        )


@api_view(["GET"])
def get_Telegram_Bot(request:HttpRequest,name:str):
    try :
        bot = TelegramBot.objects.get(name=name)
        return Response({"url":f"https://api.telegram.org/bot{bot.key}/sendMessage"})
    except Exception as e :
        return Response({
                    "success":False ,
                    "error":"Please Check your query params",
                })


@api_view(["GET"])
def get_chats_id(request:HttpRequest,name:str):
    try :
        bot = TelegramBot.objects.get(name=name)
        chats_info = ChatInfo.objects.filter(bot=bot)
        serializer_data = ChatInfoSerializer(chats_info, many=True).data
        return Response({
            "success":True ,
            "response":serializer_data
        })
    except TelegramBot.DoesNotExist:
        return Response(status=404, data={
            'success' : False ,
            'error': 'TelegramBot not found' ,
            })


class MacAddressesListAPIView(ListAPIView):
    queryset = MacAddress.objects.all()
    serializer_class = MacAddressSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated] 


class TelegramBotListAPIView(ListAPIView):
    queryset = TelegramBot.objects.all()
    serializer_class = TelegramBotSerializer
