# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from assignment.models import Users, Post
# from assignment.models import Post
from assignment.serializer.post_serializer import PostSerializer
from utility.response import ApiResponse
from utility.utils import CreateRetrieveUpdateViewSet


class PostView(CreateRetrieveUpdateViewSet, ApiResponse):
    # permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            response_data = self.get_list(self.queryset)
            return ApiResponse.response_ok(self, data=response_data)
        except Exception as e:
            return ApiResponse.response_internal_server_error(self, message=[str(e.args[0])])

    @permission_classes([IsAuthenticated])
    def post(self, request):
        try:
            authtoken= request.META['HTTP_AUTHORIZATION']
        except Exception as e:
            return ApiResponse.response_unauthenticate(self)
        try:
            instance = request.user.id
            data = {"text": request.data.get('text'), "user": request.user.id}
            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                serializer.save()
                data = self.validate(instance, serializer.data)
            else:
                msg = serializer.errors
                return ApiResponse.response_bad_request(self, message=msg)
            return ApiResponse.response_ok(self, data=data)
        except Exception as e:
            return ApiResponse.response_internal_server_error(self, message=[str(e.args[0])])

    def validate(self, instance, data):
        resp_dict = dict()
        user = Users.objects.get(id=instance)
        resp_dict['first_name'] = user.first_name
        resp_dict['last_name'] = user.last_name
        resp_dict['username'] = user.username
        data['created_by'] = resp_dict
        data.pop('user')

        return data

    def get_list_instance(self,instance):
        resp_dict = dict()
        data=dict()
        try:
            user = Users.objects.get(id=instance.id)
            data['first_name'] = user.first_name
            data['last_name'] = user.last_name
            data['username'] = user.username
        except:
            data=None
        resp_dict['id'] = instance.id
        resp_dict['text'] = instance.text
        resp_dict['created_by'] = data
        resp_dict['created_at'] = instance.created_at.timestamp()
        resp_dict['updated_at'] = instance.updated_at.timestamp()
        return resp_dict

    def get_list(self,data):
        return map(self.get_list_instance, data)
