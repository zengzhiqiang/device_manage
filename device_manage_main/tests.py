from django.test import TestCase
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", r"device_manage.settings")
import django
django.setup()

# Create your tests here.



if __name__ == "__main__":

    from device_manage_main.serializers import DeviceSerializer, DeviceDetailSerializer
    from device_manage_main.models import DeviceList, DeviceDetail
    from collections import OrderedDict
    import json

    # device = DeviceList.objects.get(pk=1)
    # '''序列化'''
    # device_serializer = DeviceSerializer(device)
    # '''反序列化'''
    # device_info = {'device_name': '弯曲疲劳试验机', 'device_name_en': 'wanqu', 'device_id': 'JG-S002', 'serial_number': 'CFT-3', 'device_model': 'B1017', 'measuring_range': '1~10000', 'accuracy': '1%', 'calibration_parameters': 'N', 'management_category': 1, 'calibration_cycle': 1}
    # device_serializer2 = DeviceSerializer(data=device_info)
    # device_serializer2.is_valid()
    # device_serializer2.save()

    # devices_2 = DeviceList.objects.all()
    # devices = DeviceList.objects.filter(device_name__contains="弯曲")
    # devices2 = DeviceList.objects.filter(device_name="冲击")
    # print(device_serializer.data)
    # device_name_list = DeviceList.objects.values_list("device_name")
    # device_name_list = DeviceList.objects.values("device_name")
    # print(device_name_list)


    # device_list = DeviceList.objects.all()
    # device_serializers = DeviceSerializer(device_list, many=True)
    # for item in device_serializers.data:
    #     print(item)
    #     data = json.loads(item, object_pairs_hook=OrderedDict)

    data = {'id': 90, 'device_name': 90, 'authorized_user': '/', 'Calibration_date': "2019-1-16", 'calibration_validity_period': "2019-1-16", 'next_calibration_date': "2019-1-16", 'calibration_company': '华测', 'certificate_number': 'JC1812857347J01-036', 'whether_stamped': '是', 'equipment_status': 1, 'internal_remarks': '/', 'remarks': '/'}
    device_detail = DeviceDetailSerializer(data=data)
    print(device_detail.is_valid())

    # print(device_detail)

    # print(device_detail.is_valid())
    # print(device_detail.data)



