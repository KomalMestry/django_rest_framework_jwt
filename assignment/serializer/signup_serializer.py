from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers, request

from assignment.models import Users
from utility.utils import generate_jwt_token


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'first_name', 'last_name', 'username', 'password']
        # fields = '__all__'
        extra_kwargs = {"password":
                            {"write_only": True}
                        }

    def create(self, validated_data):
        return Users.objects.create_user(**validated_data)
