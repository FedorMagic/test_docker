from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
import json

# Create your views here.

class TestRest(APIView):
    """
        ntc[dsjkfblsanf
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    def get(self,request):
        context = {'req':'get'}
        return Response(context)

    #@csrf_exempt
    def post(self,request, format=json):
        print(request.data)
        context = {'req':'post'}
        #return render(context)
        return Response(context, content_type='application/json')

    def options(self, request, *args, **kwargs):
        context = {'req':'options'}
        #return render(context)
        return Response(context)

    def head(self,request):
        context = {'req':'head'}
        #return render(context)
        return Response(context)

class ExampleView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)