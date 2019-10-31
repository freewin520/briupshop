from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework.decorators import api_view,schema
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.parsers import MultiPartParser
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group,Permission
# Create your views here.


# 13
def index(request):
    return HttpResponse('test index api')
# 13!
# 16
class IndexClass(APIView):
    def post(self, *args, **kwargs):
        return Response(data={'code':'200'},status=status.HTTP_200_OK)
# 16!