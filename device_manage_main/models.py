from django.db import models

# Create your models here.

class SupplierList(models.Model):
    '''供应商信息，作为外界接口'''
    supplier_name = models.CharField(verbose_name="供应商", max_length=50)

class TestMethodList(models.Model):
    '''校准规程，作为外界接口'''
    test_method_name = models.CharField(verbose_name="测试标准", max_length=50)

class ThisUserList(models.Model):
    '''用户信息，作为外界接口'''
    this_user_name = models.CharField(verbose_name="用户", max_length=50)

class DeviceList(models.Model):
    '''设备基本信息，包含设备在运行过程中不发生改变的属性'''
    MANAGEMENT_CATEGORY = (
        (1, "A类设备"),
        (2, "B类设备"),
        (3, "C类设备"),
        (4, "D类设备"),
    )
    CALIBRATION_CYCLE = (
        (1, "半年"),
        (2, "一年"),
        (3, "两年"),
        (4, "三年"),
    )

    device_name = models.CharField(verbose_name="设备名称", max_length=50)
    device_name_en = models.CharField(verbose_name="Device Name", max_length=50)
    device_id = models.CharField(verbose_name="设备编号", max_length=50)
    serial_number = models.CharField(verbose_name="出厂编号", max_length=50)
    supplier = models.ForeignKey(SupplierList, on_delete=models.CASCADE, verbose_name="制造商")
    device_model = models.CharField(verbose_name="设备型号", max_length=50)
    measuring_range = models.TextField(verbose_name="测量范围")
    accuracy = models.TextField(verbose_name="测量精度")
    calibration_procedures = models.ForeignKey(TestMethodList, on_delete=models.CASCADE, verbose_name="校准规程")
    calibration_parameters = models.TextField(verbose_name="校准参数")
    authorized_user = models.ForeignKey(ThisUserList, on_delete=models.CASCADE, verbose_name="授权使用人")
    management_category = models.IntegerField(choices=MANAGEMENT_CATEGORY, verbose_name="管理类别")
    calibration_cycle = models.IntegerField(choices=CALIBRATION_CYCLE, verbose_name="校准周期")
    start_date = models.DateField(auto_now=True, verbose_name="启用日期")

    def __str__(self):
        return self.device_name

    class Meta:
        verbose_name = "设备清单"
        verbose_name_plural = "设备清单"

class DeviceDetail(models.Model):
    '''设备详细信息。设备在运行过程中会发生改变的信息'''
    device_name = models.OneToOneField(DeviceList, on_delete=models.CASCADE, verbose_name="设备名称")
    calibration_data = models.DateField(verbose_name="校准日期")

    def __str__(self):
        device_name = self.device_name.device_name
        return device_name

    class Meta:
        verbose_name = "设备详情"
        verbose_name_plural = "设备详情"