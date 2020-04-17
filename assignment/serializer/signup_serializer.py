from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name', 'last_name', 'username', 'password']
        # fields = '__all__'
        extra_kwargs = {"password":
                            {"write_only": True}
                        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


