import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", r"device_manage.settings")
import django
django.setup()

import openpyxl

from device_manage_main.serializers import DeviceSerializer, DeviceDetailSerializer


class ImportDevice():

    def __init__(self, path):

        self.path = path
        self.workbook = openpyxl.load_workbook(path)

    def import_devices(self):
        sheet = self.workbook["设备清单"]
        mark = 0
        fields = []
        for row in sheet.values:
            if not mark:
                fields = list(row)
                mark = 1
            else:
                row_data = list(row)
                device_data = {}
                i = 0
                for field in fields:
                    device_data.update({field: row_data[i]})
                    i += 1
                device_serializer = DeviceSerializer(data=device_data)
                print(device_serializer.is_valid())
                device_serializer.save()

    def import_device_detail(self):
        sheet = self.workbook["设备详情"]
        mark = 0
        fields = []
        for row in sheet.values:
            if not mark:
                fields = list(row)
                mark = 1
            else:
                row_data = list(row)
                device_data = {}
                i = 0
                for field in fields:
                    device_data.update({field: row_data[i]})
                    i += 1
                device_detail_serializer = DeviceDetailSerializer(data=device_data)
                print(device_data)
                print(device_detail_serializer.is_valid())
                device_detail_serializer.save()

if __name__ == "__main__":

    import_device = ImportDevice("设备一览表.xlsx")
    import_device.import_devices()
    import_device.import_device_detail()


