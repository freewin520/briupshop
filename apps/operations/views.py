from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework import mixins
from .models import *
from .serializers import FavorSerializers, ShoppingCartSerializers
# Create your views here.


class FavorListView(generics.ListAPIView):
    queryset = Favor.objects.all()
    # queryset = Favor.objects.filter(user=request.user)error
    serializer_class = FavorSerializers

    # 过滤返回当前用户的收藏夹信息
    def get_queryset(self):
        # queryset = Favor.objects.filter(user = self.request.user)
        return super().get_queryset().filter(user=self.request.user)


# 加入收藏夹-新增
class FavorCreateView(generics.CreateAPIView):
    serializer_class = FavorSerializers
    # 自定义返回结果

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            # 失败信息的定制
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return Response(data={'code': 400, 'message': "收藏失败", 'error': e}, status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        # 成功后返回信息的定制

        res = Response(serializer.data, status=status.HTTP_200_OK, headers=headers)
        res.data['code'] = 200
        res.data['message'] = '收藏成功'
        return res


# 取消收藏-删除
class FavorDeleteView(generics.GenericAPIView):
    queryset = Favor.objects.all()
    serializer_class = FavorSerializers

    # 重写destroy方法自定义返回结果
    def get(self, request, pk):
        # 获取地址url中的参数
        try:
            # 自定义试图手动调用check_object_permissions(get_object())验证对象
            obj = Favor.objects.get(pk=pk)
            self.check_object_permissions(request, obj)

            Favor.objects.get(pk=pk).delete()
        except Exception as e:
            return Response(data={'code': 400, 'message': '删除失败', 'error': e}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={'code': 200, 'message': '删除成功'}, status=status.HTTP_200_OK)


# 获取单条数据详情
class FavorDetailView(generics.RetrieveAPIView):
    queryset = Favor.objects.all()
    serializer_class = FavorSerializers

# class FavorUpdateView(generics.UpdateAPIView):
#     queryset = Favor.objects.all()
#     serializer_class = FavorSerializers
#     #put:单体整改（单条数据整体修改）
#     #patch:局部修改（一条数据中的某列些值）


# 修改
# 更新收藏夹
class FavorUpdateView(generics.GenericAPIView, mixins.UpdateModelMixin):
    queryset = Favor.objects.all()
    serializer_class = FavorSerializers

    def post(self, request, *args, **kwargs):
        # print('request:',request)
        # print(kwargs)
        # 调用UpdateModelMixin中的update方法
        try:
            self.update(request, *args, **kwargs)
        except Exception as e:
            return Response(data={'code': 400, 'message': '修改失败', 'error': e}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={'code': 200, 'message': '修改成功'}, status=status.HTTP_200_OK)


class ShopCartListView(generics.ListAPIView):
    queryset = ShoppingCart.objects.all()
    # queryset = Favor.objects.filter(user=request.user)error
    serializer_class = ShoppingCartSerializers

    # 过滤返回当前用户的收藏夹信息
    def get_queryset(self):
        # queryset = Favor.objects.filter(user = self.request.user)
        return super().get_queryset().filter(user=self.request.user)


class ShopCartAddView(generics.CreateAPIView):
    serializer_class = ShoppingCartSerializers

    # 自定义返回结果
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:  # 失败信息的定制
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return Response(data={'code': 400, 'message': "无法加入购物车", 'error': e}, status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        # 成功后返回信息的定制

        res = Response(serializer.data, status=status.HTTP_200_OK, headers=headers)
        res.data['code'] = 200
        res.data['message'] = '成功加入购物车'
        return res


class ShopCartDeleteView(generics.GenericAPIView):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializers

    # 重写destroy方法自定义返回结果
    def get(self, request, pk):
        # 获取地址url中的参数
        try:
            # 使用get获取单条数据
            ShoppingCart.objects.get(pk=pk).delete()
        except:
            return Response(data={'code': 400, 'message': '删除失败'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={'code': 200, 'message': '删除成功'}, status=status.HTTP_200_OK)


class ShoppingCartDetailView(generics.RetrieveAPIView):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializers


class ShopCartUpdateView(generics.GenericAPIView,mixins.UpdateModelMixin):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializers

    def post(self, request, *args, **kwargs):
        # print('request:',request)
        # print(kwargs)
        # 调用UpdateModelMixin中的update方法
        try:
            self.update(request, *args, **kwargs)
        except:
            return Response(data={'code': 400, 'message': '修改失败'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={'code': 200, 'message': '修改成功'}, status=status.HTTP_200_OK)
