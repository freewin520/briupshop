# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, mixins
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from .filters import GoodsFilter
from goods.serializers import *
from goods.models import Goods
from goods.schemas import *
from django.http import JsonResponse

class GoodsPagination(PageNumberPagination):
    page_size = 10 #每页显示的条数
    page_size_query_param = 'page_size'
    max_page_size = 100
    page_query_param = 'p' #分页参数变量名

class GoodsListView(generics.ListAPIView):
    #{
    queryset = Goods.objects.all()#查询结果集设置
    serializer_class = GoodsListSerializer#序列器设置
    #}调用generics.ListAPIView必须有
    pagination_class = GoodsPagination#不指定就采用默认自带的分页器,采用全局配置
    #schema = GoodsListChema #指定采用的schema
    filter_backends = (DjangoFilterBackend,SearchFilter,OrderingFilter)
    filter_fields = ('name','detail')#完全匹配 采用自定义过滤器后无效果
    search_fields = ('name','detail')#模糊查询-搜索
    ordering_fields =('sale_name','actual_price') #排序
    #无需判断登录
    # permission_classes = ()
    # permission_classes = (IsAuthenticated,)#权限认证配置
    #使用自定义过滤器
    filterset_class = GoodsFilter
    def get_queryset(self):
        good_id = self.request.query_params.get('good_id','')
        if good_id:
            queryset = Goods.objects.filter(pk=good_id)#获取具体商品的信息
        else:
            queryset = Goods.objects.all()
        return queryset

#商品分类信息列表
class GoodsTypeView1(generics.ListAPIView):
    queryset = GoodsType.objects.all()
    serializer_class = GoodsTypeSerializer1
    schema = TypeListChema
    pagination_class = None#不需要分页

    def get_queryset(self):
        # type_id = self.request.data.get('type_id','')
        type_id = self.request.query_params.get('type_id', '')
        if type_id:
            queryset = GoodsType.objects.filter(id=type_id)
        else:
            queryset = GoodsType.objects.all()
        return queryset

class GoodsTypeView(generics.ListAPIView):
    queryset = GoodsType.objects.all()
    serializer_class = GoodsTypeSerializer1


        # self.request.data:POST/GET/FILES/PUT/patch 表单(schema_form) self.request.data.get('id','')
        # self.request.query_params:GET error:url:/detail/<int:id> yes:?id=1
        # htto://127.0.0.1:8000/goods/list/?page=1 yes chema_query
        # htto://127.0.0.1:8000/goods/detail/23 error
        # print('path',self.request.path) #获取请求路径
        # print(self.kwargs) 获取url中的参数值 schema_url

# class GoodsListView1(mixins.ListModelMixin,
#                         mixins.CreateModelMixin,
#                         generics.GenericAPIView):
#     queryset = Goods.objects.all()
#     serializer_class = GoodsListSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class GoodsListView2(View):
#     def get(self, request):
#         # goods = Goods.objects.all()
#         # goods_list = []
#         # for good in goods:
#         #     gooddict = {}
#         #     gooddict["name"] = good.name
#         #     gooddict["actual_price"] = good.actual_price
#         #     good_list.append(gooddict)
#         # good_list_json = json.dumps(goods_list)
#
#         goods = Goods.objects.values()
#         goods = list(goods)
#         for good in goods:
#             good["image"] = str(good["image"])
#             good["created_time"] = str(good["created_time"])
#
#         good_list_json = json.dumps(goods)
#         return HttpResponse(good_list_json)

