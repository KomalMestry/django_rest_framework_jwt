from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class LoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        data = super().validate(attrs)

        # refresh = self.get_token(self.user)

        # data['refresh_token'] = str(refresh)
        # data['access_token'] = str(refresh.access_token)
        data['refresh_token'] = data.pop('refresh')
        data['access_token'] = data.pop('access')
        return data
