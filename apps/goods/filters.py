# *_*coding:utf-8 *_*
from django_filters import rest_framework
from .models import Goods
#自定义过滤器
class GoodsFilter(rest_framework.FilterSet):
    price_min = rest_framework.NumberFilter(field_name='actual_price',lookup_expr='gte')
    price_max = rest_framework.NumberFilter(field_name='actual_price',lookup_expr='lte')

    class Meta:
        model = Goods
        fields = ['price_min','price_max']