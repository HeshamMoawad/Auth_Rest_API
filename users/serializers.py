from rest_framework.serializers import ModelSerializer
from .models import (
    MacAddress
)


class MacAddressSerializer(ModelSerializer):
    class Meta:
        model = MacAddress
        fields = ['mac_address','agent_name']
        # include = ['agent_name']
        # exclude = ["user"]










