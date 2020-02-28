from django.contrib import admin
from device_manage_main.models import DeviceList, DeviceDetail, CalibrationRecord, RepairRecord, ServerRecord

# Register your models here.


admin.site.register(DeviceList)
admin.site.register(DeviceDetail)
admin.site.register(CalibrationRecord)
admin.site.register(RepairRecord)
admin.site.register(ServerRecord)
