from rest_framework.serializers import ModelSerializer , ListSerializer
from .models import (
    MacAddress ,
    TelegramBot ,
    ChatInfo
)


class MacAddressSerializer(ModelSerializer):
    class Meta:
        model = MacAddress
        fields = ['mac_address','agent_name']



class TelegramBotSerializer(ModelSerializer):
    class Meta:
        model = TelegramBot
        fields = ['name','url']



class ChatInfoSerializer(ModelSerializer):
    class Meta:
        model = ChatInfo
        fields = ['chat_id','chat_name']






