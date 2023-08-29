from django.urls import path ,include
from .views import *

urlpatterns = [
    path('api-list-mac-address/',MacAddressesListAPIView.as_view(),name='api_list') ,
    path('api-check-exist/<str:mac_address>',check_mac_address_is_exist) ,
    path('api-check-exist/',check_mac_address_exist)
]


