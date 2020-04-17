# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from assignment.serializer.login_serializer import LoginSerializer
from utility.response import ApiResponse


class LoginView(TokenObtainPairView, ApiResponse):
    # serializer_class = LoginSerializer

    def post(self, request, attrs=None, *args, **kwargs):
        try:
            serializer_class = LoginSerializer(data=request.data)
            if serializer_class.is_valid():
                data = serializer_class.validated_data
            else:
                msg = serializer_class.errors
                return ApiResponse.response_bad_request(self, data={}, message=msg)

            return ApiResponse.response_ok(self, data=data)
        except Exception as e:
            return ApiResponse.response_internal_server_error(self, message=[str(e.args[0])])
