from rest_framework import mixins, viewsets


class CustomListRetrieveViewSet(mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    pagination_class = None
