from django.urls import path

from .views import  ContactView, ConsumerOrderView, FarmerUploadView, HomeView 

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('farmer-upload/', FarmerUploadView.as_view(), name='farmer_upload'),
    path('consumer-order/', ConsumerOrderView.as_view(), name='consumer_order'),
]
