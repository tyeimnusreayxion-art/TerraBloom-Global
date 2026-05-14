from django.db import models


class FarmerListing(models.Model):
    farm_name = models.CharField(max_length=120)
    produce_type = models.CharField(max_length=120)
    quantity = models.CharField(max_length=80)
    price_kg = models.CharField(max_length=80)
    price_bundle = models.CharField(max_length=80)
    notes = models.TextField(blank=True)
    image = models.ImageField(upload_to='produce/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.produce_type} from {self.farm_name}"


class ConsumerOrder(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('in_transit', 'In transit'),
        ('delivered', 'Delivered'),
    ]
    VEHICLE_CHOICES = [
        ('Motorbike express delivery', 'Motorbike express delivery'),
        ('Small cargo van', 'Small cargo van'),
        ('Medium truck', 'Medium truck'),
        ('Large flatbed truck', 'Large flatbed truck'),
        ('Refrigerated truck', 'Refrigerated truck'),
    ]
    buyer_name = models.CharField(max_length=120)
    buyer_email = models.EmailField()
    item = models.CharField(max_length=120)
    quantity = models.CharField(max_length=80)
    vehicle = models.CharField(max_length=80, choices=VEHICLE_CHOICES)
    details = models.TextField(blank=True)
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item} for {self.buyer_name}"


class Transaction(models.Model):
    order = models.ForeignKey(ConsumerOrder, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reference = models.CharField(max_length=120, blank=True)
    status = models.CharField(max_length=50, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reference or 'Transaction'} - {self.amount}"


class Shipment(models.Model):
    order = models.ForeignKey(ConsumerOrder, on_delete=models.SET_NULL, null=True, blank=True)
    origin = models.CharField(max_length=120)
    destination = models.CharField(max_length=120)
    vehicle = models.CharField(max_length=80)
    status = models.CharField(max_length=50, default='pending')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.order or 'Shipment'}: {self.origin} → {self.destination}"
