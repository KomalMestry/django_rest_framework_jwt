from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class CreateRetrieveUpdateViewSet(GenericViewSet,
                                  mixins.ListModelMixin,
                                  mixins.RetrieveModelMixin,
                                  mixins.CreateModelMixin,
                                  mixins.UpdateModelMixin):
    pass


