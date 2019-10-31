# *_*coding:utf-8 *_*
from rest_framework import serializers, validators

from users.models import ShopAddress


class AdsSerializers(serializers.ModelSerializer):
    # 隐藏user字段,并且赋值为当前登录用户
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = ShopAddress
        fields = "__all__"
        # fields = ('user','goods')
        # exclude = ("created_time",)
        # extra_kwargs = { #对模型已有参数重新
        #     'created_time':{'required':False, 'read_only':True}
        # }
        # 收藏夹用户和商品的联合唯一限制（验证器）
        validators = [
            validators.UniqueTogetherValidator(
                queryset=ShopAddress.objects.all(),
                fields=("user", "address")
            )
        ]
