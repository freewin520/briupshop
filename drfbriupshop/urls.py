# from django.conf.urls import url
from django.conf.urls import url
from django.contrib import admin
import rest_framework.authtoken.views
from django.urls import path,include
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='杰普商城 API')


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api_auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api_token_auth/', obtain_jwt_token),
    url(r'^api/', schema_view),
    url(r'^demo/', include('demo.urls', namespace='demo')),# demo
    path(r'goods/', include('goods.urls', namespace='goods')),# goods
    path(r'operations/', include('operations.urls', namespace='operations')),# goods
    path(r'users/', include('users.urls', namespace='users')),# users

]
