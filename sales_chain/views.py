from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from sales_chain.filters import ContactCountryFilter
from sales_chain.models import ChainLink
from sales_chain.permissions import IsActiveUserPermission
from sales_chain.serializers import ChainLinkCreateSerializer, ChainLinkSerializer


class ChainLinkViewSet(viewsets.ModelViewSet):
    permission_classes = [
        IsActiveUserPermission,
    ]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ContactCountryFilter
    queryset = ChainLink.objects.all()
    default_serializer = ChainLinkSerializer
    serializers = {
        'create': ChainLinkCreateSerializer,
        'update': ChainLinkCreateSerializer,
        'partial_update': ChainLinkCreateSerializer,
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)
