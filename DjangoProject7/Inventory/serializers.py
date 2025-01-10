from rest_framework import serializers
from .models import InventoryItem, Category, InventoryChangeLog

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class InventoryItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = InventoryItem
        fields = [
            'id', 'name', 'description', 'quantity', 'price', 'category', 'category_id',
            'date_added', 'last_updated',
        ]

class InventoryChangeLogSerializer(serializers.ModelSerializer):
    item = InventoryItemSerializer(read_only=True)
    item_id = serializers.PrimaryKeyRelatedField(
        queryset=InventoryItem.objects.all(), source='item', write_only=True
    )

    class Meta:
        model = InventoryChangeLog
        fields = ['id', 'item', 'quantity_change', 'updated_by', 'timestamp', 'item_id']