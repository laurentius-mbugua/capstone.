from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, InventoryItemViewSet, InventoryChangeLogViewSet

# Using a DRF Router for automatic URL routing
router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='category')
router.register('items', InventoryItemViewSet, basename='inventoryitem')
router.register('changelog', InventoryChangeLogViewSet, basename='inventorychangelog')

urlpatterns = [
    path('api/', include(router.urls)),
]
