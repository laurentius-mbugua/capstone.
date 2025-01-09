from rest_framework import serializers
from .models import InventoryItem, Category, InventoryChangeLog


# Serializer for Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


# Serializer for InventoryItem
class InventoryItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  # Nest category details (or use ID instead)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = InventoryItem
        fields = [
            'id', 'name', 'description', 'quantity', 'price', 'category', 'category_id',
            'date_added', 'last_updated',
        ]


# Serializer for InventoryChangeLog
class InventoryChangeLogSerializer(serializers.ModelSerializer):
    item = InventoryItemSerializer(read_only=True)  # Link with item
    item_id = serializers.PrimaryKeyRelatedField(
        queryset=InventoryItem.objects.all(), source='item', write_only=True
    )

    class Meta:
        model = InventoryChangeLog
        fields = ['id', 'item', 'quantity_change', 'updated_by', 'timestamp', 'item_id']
