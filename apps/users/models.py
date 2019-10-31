from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# 收货地址
class ShopAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=60, verbose_name='收货人姓名')
    tel = models.CharField(max_length=20, verbose_name='联系方式')
    address = models.CharField(max_length=255, verbose_name='收货地址')
    zipcode = models.IntegerField(verbose_name='邮编')
    is_default = models.BooleanField(default=False, verbose_name='是否默认')

    class Meta():
        verbose_name = '收货地址'

    def __str__(self):
        return self.name


class UserInfo(models.Model):
    STATUS = (
        (1, '女'),
        (2, '男')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.IntegerField(choices=STATUS, verbose_name='用户性别')
    picture = models.ImageField(upload_to='uploads/user/%Y/', verbose_name='用户头像')
