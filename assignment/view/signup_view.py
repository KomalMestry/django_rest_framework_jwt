# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from assignment.serializer.signup_serializer import SignUpSerializer
from utility.response import ApiResponse
from utility.utils import CreateRetrieveUpdateViewSet, generate_jwt_token


class SignUpView(CreateRetrieveUpdateViewSet, ApiResponse):
    serializer_class = SignUpSerializer

    def post(self, request):
        try:
            resp_dict=dict()
            host = request.get_host()
            response= self.create(request)
            username=request.data.get('username')
            password=request.data.get('password')
            chk_user = authenticate(username=username, password=password)
            if chk_user:
                token = generate_jwt_token(host, username, password)
                if token.status_code == 200:
                    resp_dict['token'] = token.json()
                    return ApiResponse.response_ok(self,data=token.json())
                return ApiResponse.response_bad_request(self)
            return ApiResponse.response_bad_request(self)
        except Exception as e:
            return ApiResponse.response_internal_server_error(self, message=[str(e.args[0])])
