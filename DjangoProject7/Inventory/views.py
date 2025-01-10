from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import InventoryItem, Category, InventoryChangeLog
from .serializers import InventoryItemSerializer, CategorySerializer, InventoryChangeLogSerializer
from .permissions import IsOwnerOrReadOnly
from django.http import HttpResponse


def home(request):
    return HttpResponse("This project works!")

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        instance = serializer.save()
        if 'quantity' in serializer.validated_data:
            InventoryChangeLog.objects.create(
                item=instance,
                quantity_change=serializer.validated_data['quantity'] - instance.quantity,
                updated_by=self.request.user
            )

class InventoryChangeLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InventoryChangeLog.objects.all()
    serializer_class = InventoryChangeLogSerializer
    permission_classes = [IsAuthenticated]