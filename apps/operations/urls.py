from django.urls import path

from operations import views

app_name = '[operations]'
urlpatterns = [
    # 收藏夹列表
    path(r'favorlist/', views.FavorListView.as_view(), name='favorlist'),
    # 添加收藏
    path(r'favorcreate/', views.FavorCreateView.as_view(), name='favorcreate'),
    # 取消收藏
    path(r'favordelete/<int:pk>/', views.FavorDeleteView.as_view(), name='favordelete'),
    # 获取单条数据详情
    path(r'favordetail/<int:pk>/', views.FavorDetailView.as_view(), name='favordetail'),
    # 修改-编辑收藏夹
    path(r'favorupdate/<int:pk>',views.FavorUpdateView.as_view(),name='favorupdate'),
    # 购物车列表
    path(r'shopcartlist/',views.ShopCartListView.as_view(),name='shopcartlist'),
    # 加入购物车
    path(r'shopcartadd/',views.ShopCartAddView.as_view(),name='shopcartadd'),
    # 删除购物车
    path(r'shopcartdelete<int:pk>/',views.ShopCartDeleteView.as_view(),name='shopcartdelete'),
    # 获取单条购物车数据
    path(r'shopcartdetail/<int:pk>/', views.ShoppingCartDetailView.as_view(), name='shopcartdetail'),
    # 修改-编辑购物车
    path(r'shopcartupdate/<int:pk>/',views.ShopCartUpdateView.as_view(),name='shopcartupdate')
]