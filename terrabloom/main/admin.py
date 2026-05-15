from django.contrib import admin

from .models import ConsumerOrder, FarmerListing, Shipment, Transaction


@admin.register(FarmerListing)
class FarmerListingAdmin(admin.ModelAdmin):
    list_display = ('farm_name', 'produce_type', 'quantity', 'price_kg', 'price_bundle', 'created_at')
    search_fields = ('farm_name', 'produce_type')


@admin.register(ConsumerOrder)
class ConsumerOrderAdmin(admin.ModelAdmin):
    list_display = ('item', 'buyer_name', 'buyer_email', 'quantity', 'vehicle', 'status', 'created_at')
    list_filter = ('status', 'vehicle')
    search_fields = ('item', 'buyer_name', 'buyer_email')


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('reference', 'order', 'amount', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('reference',)


@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('order', 'origin', 'destination', 'vehicle', 'status', 'updated_at')
    list_filter = ('status', 'vehicle')
    search_fields = ('origin', 'destination')
