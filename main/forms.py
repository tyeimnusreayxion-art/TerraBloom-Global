from django import forms
from .models import ConsumerOrder, FarmerListing


class FarmerListingForm(forms.ModelForm):
    class Meta:
        model = FarmerListing
        fields = ['farm_name', 'produce_type', 'quantity', 'price_kg', 'price_bundle', 'notes', 'image']
        widgets = {
            'notes': forms.Textarea(attrs={'placeholder': 'Tell buyers about your growing methods, expected delivery windows, or special offers'}),
        }


class ConsumerOrderForm(forms.ModelForm):
    buyer_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your full name'}))
    buyer_email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'you@example.com'}))
    item = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'What goods do you need?'}))
    quantity = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'e.g. 50 kg, 20 crates, 10 bundles'}))
    vehicle = forms.ChoiceField(choices=ConsumerOrder.VEHICLE_CHOICES)
    details = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Special handling, delivery location, or timing preferences'}), required=False)

    class Meta:
        model = ConsumerOrder
        fields = ['buyer_name', 'buyer_email', 'item', 'quantity', 'vehicle', 'details']
