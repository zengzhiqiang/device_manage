from django.contrib import admin
from device_manage_main.models import SupplierList, TestMethodList, ThisUserList, DeviceList, DeviceDetail

# Register your models here.

admin.site.register(SupplierList)
admin.site.register(TestMethodList)
admin.site.register(ThisUserList)
admin.site.register(DeviceList)
admin.site.register(DeviceDetail)
