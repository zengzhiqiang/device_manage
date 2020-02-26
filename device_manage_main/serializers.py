from rest_framework import serializers
from device_manage_main.models import DeviceList, DeviceDetail

class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeviceList
        fields = "__all__"
        # exclude = ["data"]

class DeviceDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeviceDetail
        fields = "__all__"