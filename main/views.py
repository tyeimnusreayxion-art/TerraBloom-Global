from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth import views as auth_views

from .forms import ConsumerOrderForm, FarmerListingForm
from .models import ConsumerOrder, Shipment, Transaction


class HomeView(TemplateView):
    template_name = 'index.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class FarmerUploadView(CreateView):
    template_name = 'farmer_upload.html'
    form_class = FarmerListingForm
    success_url = reverse_lazy('farmer_upload')


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