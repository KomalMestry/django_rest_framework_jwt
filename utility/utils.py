from django.conf import settings
from django.contrib.sites import requests
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class CreateRetrieveUpdateViewSet(GenericViewSet,
                                  mixins.ListModelMixin,
                                  mixins.RetrieveModelMixin,
                                  mixins.CreateModelMixin,
                                  mixins.UpdateModelMixin):
    pass


""" token generations by oauth """


def generate_oauth_token(host, username, password):
    client_id = settings.CLIENT_ID
    client_secret = settings.CLIENT_SECRET
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'grant_type': 'password',
               'username': username,
               'password': password,
               'client_id': client_id,
               'client_secret': client_secret}
    return (requests.post(settings.SERVER_PROTOCOLS + host + "/o/token/",
                          data=payload, headers=headers))


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
    return (requests.post(settings.SERVER_PROTOCOLS + host + "api/token/",
                          data=payload, headers=headers))
