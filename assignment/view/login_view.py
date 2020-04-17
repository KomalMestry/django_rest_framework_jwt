# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth import authenticate
from django.shortcuts import render
# from assignment.serializer.login_serializer import LoginSerializer
from assignment.models import Users
from utility.response import ApiResponse
from utility.utils import generate_jwt_token, CreateRetrieveUpdateViewSet


class LoginView(CreateRetrieveUpdateViewSet,ApiResponse):

    def post(self, request, *args, **kwargs):
        try:
            resp_dict=dict()
            host = request.get_host()
            username = request.data.get('username')
            password = request.data.get('password')

            if not username or not password:
                return ApiResponse.response_bad_request(self, message="Username and Password are required")

            """ authenticate user and generate token """
            # user = authenticate(self, username=username, password=password)
            user = Users.objects.get(username=username)
            if user.check_password(password):
                # token = user.create_jwt()
                """
                Authorize to user
                """
                token = generate_jwt_token(host, username, password)
                if token.status_code == 200:
                    resp_dict['token'] = token.json()
                    return ApiResponse.response_ok(self, data=token.json(), message="Login successful")
                return ApiResponse.response_bad_request(self, message="User Not Authorized")
            return ApiResponse.response_unauthorized(self, message="Invalid username or password. Please try again.")

        except Exception as e:
            return ApiResponse.response_internal_server_error(self, message=[str(e.args[0])])


