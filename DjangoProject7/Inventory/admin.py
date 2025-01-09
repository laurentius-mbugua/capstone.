from django.contrib import admin
from .models import InventoryItem, Category, InventoryChangeLog


# Register the InventoryItem model
@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'price', 'category', 'owner', 'date_added', 'last_updated')
    list_filter = ('category', 'owner', 'date_added')  # Filters on the side
    search_fields = ('name', 'description')  # Search by name and description


# Register the Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


# Register the InventoryChangeLog model
@admin.register(InventoryChangeLog)
class InventoryChangeLogAdmin(admin.ModelAdmin):
    list_display = ('item', 'quantity_change', 'updated_by', 'timestamp')
    list_filter = ('timestamp', 'updated_by')  # Filters on the side
    search_fields = ('item__name',)  # Enable search based on related InventoryItem name
