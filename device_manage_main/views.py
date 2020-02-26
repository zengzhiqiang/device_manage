# import os
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", r"device_manage.settings")
# import django
#
# django.setup()





from rest_framework import viewsets
from device_manage_main.models import DeviceList, DeviceDetail
from device_manage_main.serializers import DeviceSerializer, DeviceDetailSerializer
from rest_framework.views import APIView
from django.http import Http404, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
import re

class DeviceViewSet(viewsets.ModelViewSet):

    queryset = DeviceList.objects.all()
    serializer_class = DeviceSerializer

class DeviceDetailViewSet(viewsets.ModelViewSet):
    queryset = DeviceDetail.objects.all()
    serializer_class = DeviceDetailSerializer

class DeviceSearchView(APIView):

    # def get_like_str(self, search_str):
    #     '''获取包含搜索字符串的相关列表'''
    #     like_str = []
    #     device_name_list = DeviceList.objects.values_list("device_name")
    #     # print(device_name_list)
    #     device_id_list = DeviceList.objects.values_list("device_id")
    #     for device_name in device_name_list:
    #         if search_str in device_name[0]:
    #             if device_name[0] not in like_str:
    #                 like_str.append(device_name[0])
    #     for device_id in device_id_list:
    #         if search_str in device_id[0]:
    #             if device_id[0] not in like_str:
    #                 like_str.append(device_id[0])
    #     return like_str

    def get_devices(self, search_str):
        '''在设备名称中搜索相关名称'''
        if search_str:
            return (DeviceList.objects.filter(device_name__icontains=search_str) or
                    DeviceList.objects.filter(device_id__icontains=search_str))
        else:
            raise Http404

    def get(self, request, search_str, format=None):

        devices = self.get_devices(search_str)
        devices_serializers = DeviceSerializer(devices, many=True)
        return Response(devices_serializers.data)

# if __name__ == "__main__":
#
#     pass
