from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import ConsumerOrderForm, FarmerListingForm
from .models import ConsumerOrder, FarmerListing, Shipment, Transaction


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['listings'] = FarmerListing.objects.order_by('-created_at')[:6]
        return context


class ContactView(TemplateView):
    template_name = 'contact.html'


class FarmerUploadView(CreateView):
    template_name = 'farmer_upload.html'
    form_class = FarmerListingForm
    success_url = reverse_lazy('farmer_upload')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_listings'] = FarmerListing.objects.order_by('-created_at')[:6]
        return context


class ConsumerOrderView(CreateView):
    template_name = 'consumer_order.html'
    form_class = ConsumerOrderForm
    success_url = reverse_lazy('consumer_order')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = ConsumerOrder.objects.order_by('-created_at')[:8]
        context['transactions'] = Transaction.objects.order_by('-created_at')[:8]
        context['shipments'] = Shipment.objects.order_by('-updated_at')[:8]
        context['order_total'] = ConsumerOrder.objects.count()
        context['transaction_total'] = Transaction.objects.count()
        context['shipment_total'] = Shipment.objects.filter(status='in_transit').count()
        context['active_buyers'] = ConsumerOrder.objects.values('buyer_email').distinct().count()
        return context


class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = ConsumerOrder.objects.order_by('-created_at')[:10]
        context['transactions'] = Transaction.objects.order_by('-created_at')[:10]
        context['shipments'] = Shipment.objects.order_by('-updated_at')[:10]
        context['listings'] = FarmerListing.objects.order_by('-created_at')[:10]
        context['order_total'] = ConsumerOrder.objects.count()
        context['transaction_total'] = Transaction.objects.count()
        context['shipment_total'] = Shipment.objects.filter(status='in_transit').count()
        context['active_buyers'] = ConsumerOrder.objects.values('buyer_email').distinct().count()
        context['listing_total'] = FarmerListing.objects.count()
        context['pending_orders'] = ConsumerOrder.objects.filter(status='pending').count()
        return context
