from django.urls import path
from trading.views import (
    ContactsViewSet,
    ProductsViewSet,
    RetailNetworkViewSet,
    TraderViewSet,
    FactoryListAPIView,
    FactoryViewSet,
    RetailNetworkListAPIView,
    TraderListAPIView

)
from trading.apps import TradingConfig
from rest_framework.routers import DefaultRouter

app_name = TradingConfig.name

router = DefaultRouter()
router.register(r'contacts', ContactsViewSet, basename='contacts')
router.register(r'products', ProductsViewSet, basename='products')
router.register(r'factories', FactoryViewSet, basename='factories')
router.register(r'retail_network', RetailNetworkViewSet, basename='retail_network')
router.register(r'traders', TraderViewSet, basename='traders')


urlpatterns = [
    path('factories/list/', FactoryListAPIView.as_view(), name='factories_list'),
    path('retail_network/list/', RetailNetworkListAPIView.as_view(), name='retail_network_list'),
    path('traders/list/', TraderListAPIView.as_view(), name='traders_list'),
]+router.urls
