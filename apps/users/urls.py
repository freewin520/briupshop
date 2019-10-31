from django.urls import path
from .views import *

app_name = '[users]'
urlpatterns = [
    path(r'adslist/', AdsListView.as_view(), name='adslist'),
    path(r'adscreate/', AdsCreateView.as_view(), name='adscreate'),
    path(r'adsdelete/<int:pk>/', AdsDeleteView.as_view(), name='adsdelete'),
    path(r'adsdetail/<int:pk>/', AdsDetailView.as_view(), name='adsdetail'),
    # 修改-编辑
    path(r'adsupdate/<int:pk>', AdsUpdateView.as_view(), ame='adsupdate')
]
