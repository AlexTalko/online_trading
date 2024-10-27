from django_filters import rest_framework as filters
from trading.models import Factory, RetailNetwork, Trader


class BaseCountryFilter(filters.FilterSet):
    """Базовый класс для фильтрации по стране"""
    exact_country = filters.CharFilter(field_name='contacts__country', lookup_expr='icontains')

    class Meta:
        abstract = True
        fields = ['contacts__country']


class FactoryCountryFilter(BaseCountryFilter):

    class Meta(BaseCountryFilter.Meta):
        model = Factory


class RetailNetworkCountryFilter(BaseCountryFilter):

    class Meta(BaseCountryFilter.Meta):
        model = RetailNetwork


class TraderCountryFilter(BaseCountryFilter):

    class Meta(BaseCountryFilter.Meta):
        model = Trader
