from django.conf import settings
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
import requests


class CreateRetrieveUpdateViewSet(GenericViewSet,
                                  mixins.ListModelMixin,
                                  mixins.RetrieveModelMixin,
                                  mixins.CreateModelMixin,
                                  mixins.UpdateModelMixin):
    pass


""" token generations by jwt """


def generate_jwt_token(host, username, password):
    headers = {
        "typ": "JWT",
        "alg": "HS256"
    }
    payload = {"token_type": "access",
               "exp": 1543828431,
               'username': username,
               'password': password,
               }
    return (requests.post(settings.SERVER_PROTOCOLS + host + "/api/token/",
                          data=payload, headers=headers))
