from django.contrib import admin
from .models import FarmerListing, ConsumerOrder, Transaction, Shipment


@admin.register(FarmerListing)
class FarmerListingAdmin(admin.ModelAdmin):
    list_display = ('farm_name', 'produce_type', 'quantity', 'price_kg', 'price_bundle', 'created_at')
    search_fields = ('farm_name', 'produce_type')
    list_filter = ('created_at',)


@admin.register(ConsumerOrder)
class ConsumerOrderAdmin(admin.ModelAdmin):
    list_display = ('buyer_name', 'buyer_email', 'item', 'quantity', 'vehicle', 'status', 'created_at')
    search_fields = ('buyer_name', 'buyer_email', 'item')
    list_filter = ('status', 'vehicle', 'created_at')
    list_editable = ('status',)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('reference', 'order', 'amount', 'status', 'created_at')
    search_fields = ('reference',)
    list_filter = ('status', 'created_at')


@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('order', 'origin', 'destination', 'vehicle', 'status', 'updated_at')
    search_fields = ('origin', 'destination')
    list_filter = ('status', 'vehicle')
    list_editable = ('status',)
