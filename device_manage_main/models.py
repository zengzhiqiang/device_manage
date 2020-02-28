from django.db import models

# Create your models here.

'''
设备清单 DeviceList
设备详情 DeviceDetail
设备校准记录 
设备维护记录 
设备维修记录 
'''

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
    supplier_id = models.CharField(verbose_name="生产厂家", max_length=100)
    device_model = models.CharField(verbose_name="设备型号", max_length=50)
    measuring_range = models.TextField(verbose_name="测量范围")
    accuracy = models.TextField(verbose_name="测量精度")
    calibration_parameters = models.TextField(verbose_name="校准参数")
    calibration_procedures = models.TextField(verbose_name="校准规程")
    management_category = models.IntegerField(choices=MANAGEMENT_CATEGORY, verbose_name="管理类别")
    calibration_cycle = models.IntegerField(choices=CALIBRATION_CYCLE, verbose_name="校准周期")
    start_date = models.DateField(auto_now=True, verbose_name="启用日期")

    def __str__(self):
        name = self.device_id + " " + self.device_name
        return name

    class Meta:
        verbose_name = "设备清单"
        verbose_name_plural = "设备清单"
        ordering = ["id"]

class DeviceDetail(models.Model):

    EQUIPMENT_STATUS = (
        (1, "完好"),
        (2, "限制使用"),
        (3, "暂停使用"),
        (4, "报废"),
    )

    device_name = models.ForeignKey("DeviceList", on_delete=models.CASCADE, verbose_name="设备名称")
    authorized_user = models.CharField(verbose_name="使用授权人", max_length=100)
    Calibration_date = models.DateField(verbose_name="校准日期", auto_now=False)
    calibration_validity_period = models.DateField(verbose_name="校准有效期", auto_now=False)
    next_calibration_date = models.DateField(verbose_name="下次校准日期", auto_now=False)
    calibration_company = models.CharField(verbose_name="校准公司", max_length=100)
    certificate_number = models.CharField(verbose_name="证书编号", max_length=100)
    whether_stamped = models.CharField(verbose_name="是否盖章", max_length=100)
    equipment_status = models.IntegerField(verbose_name="设备状态", choices=EQUIPMENT_STATUS)
    internal_remarks = models.TextField("内部备注")
    remarks = models.TextField("备注")

    def __str__(self):
        name = self.device_name.device_id + " " + self.device_name.device_name
        return name

    class Meta:
        verbose_name = "设备详情"
        verbose_name_plural = "设备详情"
        ordering = ["id"]

class CalibrationRecord(models.Model):

    '''
    设备校准记录表单，每一台设备校准一次都需要在该表单内记录信息
    默认将最后一次校准信息返回
    查询历史校准信息
    '''

    device_name = models.ForeignKey("DeviceList", on_delete=models.CASCADE, verbose_name="设备名称")

    def __str__(self):
        name = self.device_name.device_id + " " + self.device_name.device_name
        return name

    class Meta:
        verbose_name = "校准记录"
        verbose_name_plural = "校准记录"
        # ordering = ["id"]

class RepairRecord(models.Model):

    '''
    设备维修记录表单，每一台设备维修一次都需要在该表单内记录信息
    默认将最后一次维修信息返回
    查询历史维修信息
    '''

    device_name = models.ForeignKey("DeviceList", on_delete=models.CASCADE, verbose_name="设备名称")

    def __str__(self):
        name = self.device_name.device_id + " " + self.device_name.device_name
        return name

    class Meta:
        verbose_name = "维修记录"
        verbose_name_plural = "维修记录"
        # ordering = ["id"]

class ServerRecord(models.Model):

    '''
    设备维护记录表单，每一台设备维护一次都需要在该表单内记录信息
    默认将最后一次维护信息返回
    查询历史维护信息
    '''

    device_name = models.ForeignKey("DeviceList", on_delete=models.CASCADE, verbose_name="设备名称")

    def __str__(self):
        name = self.device_name.device_id + " " + self.device_name.device_name
        return name

    class Meta:
        verbose_name = "维护记录"
        verbose_name_plural = "维护记录"
        # ordering = ["id"]