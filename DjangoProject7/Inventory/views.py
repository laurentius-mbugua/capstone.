from rest_framework import generics, viewsets
from .models import InventoryItem, Category, InventoryChangeLog
from .serializers import InventoryItemSerializer, CategorySerializer, InventoryChangeLogSerializer


# CRUD for Category
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# CRUD for InventoryItem
class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer


# CRUD for InventoryChangeLog
class InventoryChangeLogViewSet(viewsets.ModelViewSet):
    queryset = InventoryChangeLog.objects.all()
    serializer_class = InventoryChangeLogSerializer
