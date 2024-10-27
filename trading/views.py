from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend
from trading.models import Contacts, Products, Factory, RetailNetwork, Trader
from trading.serializers import (
    ContactsSerializer,
    ProductsSerializer,
    FactorySerializer,
    RetailNetworkSerializer,
    TraderSerializer,
)
from trading.filters import (
    FactoryCountryFilter,
    RetailNetworkCountryFilter,
    TraderCountryFilter
)
from trading.paginators import CustomPagination


class ContactsViewSet(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        contacts = serializer.save()
        contacts.save()
        return contacts


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        products = serializer.save()
        products.save()
        return products


class FactoryViewSet(viewsets.ModelViewSet):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        factory = serializer.save()
        factory.save()
        return factory


class FactoryListAPIView(generics.ListAPIView):
    """Cписок всех экземпляров Factory"""
    queryset = Factory.objects.all().order_by("name")
    serializer_class = FactorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = FactoryCountryFilter
    pagination_class = CustomPagination


class RetailNetworkViewSet(viewsets.ModelViewSet):
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        retail_network = serializer.save()
        retail_network.save()
        return retail_network


class RetailNetworkListAPIView(generics.ListAPIView):
    """Cписок всех экземпляров RetailNetwork"""
    queryset = RetailNetwork.objects.all().order_by("name")
    serializer_class = RetailNetworkSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RetailNetworkCountryFilter
    pagination_class = CustomPagination


class TraderViewSet(viewsets.ModelViewSet):
    queryset = Trader.objects.all()
    serializer_class = TraderSerializer
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        trader = serializer.save()
        trader.save()
        return trader


class TraderListAPIView(generics.ListAPIView):
    """Cписок всех экземпляров Trader"""
    queryset = Trader.objects.all().order_by('name')
    serializer_class = TraderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TraderCountryFilter
    pagination_class = CustomPagination
