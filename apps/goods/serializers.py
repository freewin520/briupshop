# *_*coding:utf-8 *_*
from rest_framework import serializers
# 商品列表序列化
from goods.models import *


class GoodsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsType
        fields = "__all__"


class GdisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsDisplayFiles
        fields = '__all__'


class GoodsListSerializer(serializers.ModelSerializer):
    one_typename = GoodsTypeSerializer() # 一访问一(外表找主表)
    two_typename = GoodsTypeSerializer()
    three_typename = GoodsTypeSerializer()
    img = GdisplaySerializer(many=True) # related_name 一找多（主表找外表）

    class Meta:
        model = Goods
        # 不包含
        exclude = ('name',)
        # fields = ('name','actual_price','')#包含
        fields = "__all__"


class GoodListSerializer1(serializers.Serializer):
    name = serializers.CharField(required="True")
    actual_price = serializers.IntegerField(required=True)


# 商品分类信息
class GoodsTypeSerializer3(serializers.ModelSerializer):
    class Meta:
        model = GoodsType
        fields = "__all__"


class GoodsTypeSerializer2(serializers.ModelSerializer):
    son = GoodsTypeSerializer3(many=True)

    class Meta:
        model = GoodsType
        fields = "__all__"


class GoodsTypeSerializer1(serializers.ModelSerializer):
    son = GoodsTypeSerializer2(many=True)

    class Meta:
        model = GoodsType
        fields = "__all__"
