from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

from goods.models import Goods
from users.models import ShopAddress


# Create your models here.
class Orders(models.Model):
    ORDER_STATUS = (
        (1, '未付款'),
        (2, '待发货'),
        (3, '运输中'),
        (4, '已收货')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(ShopAddress, on_delete=models.CASCADE)
    status = models.IntegerField(choices=ORDER_STATUS, verbose_name='订单状态')
    order_time = models.DateTimeField(verbose_name='下单时间')
    total_price = models.FloatField(verbose_name='订单总价')

    class Meta():
        verbose_name = '订单表'

    def __str__(self):
        return self.status


class OrderGoodShip(models.Model):
    orders = models.ForeignKey(Orders, on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    numbers = models.IntegerField()

    class Meta():
        verbose_name = '订单详情表'

    def __str__(self):
        return self.numbers


class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    numbers = models.IntegerField()
    created_time = models.DateTimeField(auto_now=True)

    class Meta():
        verbose_name = '商品信息表'

    def __str__(self):
        return self.numbers


class Favor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    created_time = models.DateTimeField(default=datetime.now())

    class Meta():
        verbose_name = '收藏夹'

    def __str__(self):
        return self.created_time


class Comments(models.Model):
    STAR = (
        (1, '一星级'),
        (2, '二星级'),
        (3, '三星级'),
        (4, '四星级'),
        (5, '五星级')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    orders = models.ForeignKey(Orders, on_delete=models.CASCADE)
    text = models.CharField(max_length=255, verbose_name='评论')
    star = models.IntegerField(choices=STAR, verbose_name='星级')
    created_time = models.DateTimeField()
