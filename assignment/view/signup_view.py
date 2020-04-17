# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from assignment.serializer.signup_serializer import SignUpSerializer
from utility.response import ApiResponse
from utility.utils import CreateRetrieveUpdateViewSet


class SignUpView(CreateRetrieveUpdateViewSet, ApiResponse):
    serializer_class = SignUpSerializer

    def post(self, request):
        try:
            response= self.create(request)
            return ApiResponse.response_ok(self,data=response.data)
        except Exception as e:
            return ApiResponse.response_internal_server_error(self, message=[str(e.args[0])])
