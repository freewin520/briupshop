# *_*coding:utf-8 *_*
from rest_framework import serializers, validators
from .models import *


class FavorSerializers(serializers.ModelSerializer):
    # 隐藏user字段,并且赋值为当前登录用户
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Favor
        fields = "__all__"
        # fields = ('user','goods')
        # exclude = ("created_time",)
        extra_kwargs = {
            # 对模型已有参数重新
            'created_time': {'required': False, 'read_only': True}
        }
        # 收藏夹用户和商品的联合唯一限制（验证器）
        validators = [
            validators.UniqueTogetherValidator(
                queryset=Favor.objects.all(),
                fields=("user", "goods")
            )
        ]


class ShoppingCartSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = ShoppingCart
        fields = "__all__"
        # fields = ('user','goods')
        # exclude = ("created_time",)
        extra_kwargs = {  # 对模型已有参数重新
            'created_time': {'read_only': True}
        }
