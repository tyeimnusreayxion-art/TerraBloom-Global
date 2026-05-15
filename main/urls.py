from django.urls import path
from .views import ContactView, ConsumerOrderView, FarmerUploadView, HomeView, DashboardView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('order/', ConsumerOrderView.as_view(), name='consumer_order'),
    path('farmer-upload/', FarmerUploadView.as_view(), name='farmer_upload'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
