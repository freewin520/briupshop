from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.shortcuts import render
from .models import User

# Create your views here.
from rest_framework import generics, status, mixins, permissions
from rest_framework.response import Response

from users.serializers import AdsSerializers
from .models import ShopAddress


# 地址列显示
class AdsListView(generics.ListAPIView):
    queryset = ShopAddress.objects.all()
    # queryset = Favor.objects.filter(user=request.user)error
    serializer_class = AdsSerializers
    # 过滤返回当前用户的收藏夹信息

    def get_queryset(self):
        # queryset = Favor.objects.filter(user = self.request.user)
        return super().get_queryset().filter(user=self.request.user)


# 地址增加
class AdsCreateView(generics.CreateAPIView):
    serializer_class = AdsSerializers
    # 自定义返回结果

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            # 失败信息的定制
            serializer.is_valid(raise_exception=True)
        except:
            return Response(data={'code':400,'message':"收藏失败"},status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        # 成功后返回信息的定制
        res = Response(serializer.data,status=status.HTTP_200_OK,headers=headers)
        res.data['code'] = 200
        res.data['message'] = '收藏成功'
        return res


# 地址删除
class AdsDeleteView(generics.GenericAPIView):
    queryset = ShopAddress.objects.all()
    serializer_class = AdsSerializers

    # 重写destroy方法自定义返回结果
    def get(self, request, pk):
        # 获取地址url中的参数
        try:
            # 使用get获取单条数据
            for i in pk:
                ShopAddress.objects.get(pk=i).delete()
        except:
            return Response(data={'code':400,'message':'删除失败'},status=status.HTTP_400_BAD_REQUEST)
        return Response(data={'code':200,'message':'删除成功'},status=status.HTTP_200_OK)


# 单条查询
class AdsDetailView(generics.RetrieveAPIView):
    queryset = ShopAddress.objects.all()
    serializer_class = AdsSerializers


# 地址修改
class AdsUpdateView(generics.GenericAPIView,mixins.UpdateModelMixin):
    queryset = ShopAddress.objects.all()
    serializer_class = AdsSerializers

    def post(self, request, *args, **kwargs):
        # print('request:',request)
        # print(kwargs)
        # 调用UpdateModelMixin中的update方法
        try:
            self.update(request, *args, **kwargs)
        except:
            return Response(data={'code': 400, 'message': '修改失败'},status=status.HTTP_400_BAD_REQUEST)
        return Response(data={'code': 200, 'message': '修改成功'}, status=status.HTTP_200_OK)


def jwt_response_payload_handler(token, user=None, request=None):
    # 通过用户user对象即可获取用户相关权限等其他信息
    return{
        'token': token,
        'user': user.username,
        'test': 'test'
    }


# 自定义登录验证
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except:
            return None


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    对象级权限，仅允许对象的所有者编辑它。
    假设模型实例具有 `owner` 属性。
    """

    def has_object_permission(self, request, view, obj):
        # 任何请求都允许读取权限，
        # 所以我们总是允许 GET，HEAD 或 OPTIONS 请求。
        # if request.method in permissions.SAFE_METHODS:
        #     return True

        # 实例必须具有名为 `owner` 的属性。
        return obj.owner == request.user



