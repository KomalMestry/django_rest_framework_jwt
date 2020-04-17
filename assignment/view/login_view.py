# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from assignment.serializer.login_serializer import LoginSerializer
from utility.response import ApiResponse
from utility.utils import generate_jwt_token


class LoginView(TokenObtainPairView, ApiResponse):
    # serializer_class = LoginSerializer

    # def post(self, request, attrs=None, *args, **kwargs):
    #     try:
    #         serializer_class = LoginSerializer(data=request.data)
    #         if serializer_class.is_valid():
    #             data = serializer_class.validated_data
    #         else:
    #             msg = serializer_class.errors
    #             return ApiResponse.response_bad_request(self, data={}, message=msg)
    #
    #         return ApiResponse.response_ok(self, data=data)
    #     except Exception as e:
    #         return ApiResponse.response_internal_server_error(self, message=[str(e.args[0])])

    def post(self, request, *args, **kwargs):
        try:
            # import ipdb;ipdb.set_trace()
            host = request.get_host()
            username = request.data.get('username')
            password = request.data.get('password')

            if not username or not password:
                return ApiResponse.response_bad_request(self, message="Username and Password are required")

            """ authenticate user and generate token """
            user = authenticate(self, username=username, password=password)

            if user:
                """
                Authorize to user
                """
                # token = generate_token(request, user)
                token = generate_jwt_token(host, username, password)
                if token.status_code == 200:
                    # resp_dict = get_login_response(user, token)
                    # resp_dict['token'] = token.json()
                    return ApiResponse.response_ok(self, data={}, message="Login successful")
                else:
                    return ApiResponse.response_bad_request(self, message="User Not Authorized")
            else:
                return ApiResponse.response_unauthorized(self, message="Invalid username or password. Please try again.")

        except Exception as e:
            return ApiResponse.response_internal_server_error(self, message=[str(e.args[0])])
