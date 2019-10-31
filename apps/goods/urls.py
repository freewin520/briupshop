from django.conf.urls import url
from django.urls import path

from goods import views

app_name = '[goods]'
urlpatterns = [
    path(r'list/<int:id>', views.GoodsListView.as_view(), name='list'),
    # path(r'typelist/',views.GoodsTypeView.as_view(),name='typelist')
    path('typelist/', views.GoodsTypeView.as_view(), name='typelist'),
]
