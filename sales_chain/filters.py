from django_filters import CharFilter
from django_filters.rest_framework import FilterSet

from sales_chain.models import ChainLink


class ContactCountryFilter(FilterSet):
    country: CharFilter = CharFilter(
        field_name='contact__country',
        lookup_expr='icontains',
    )

    class Meta:
        model = ChainLink
        fields = ('contact__country',)
