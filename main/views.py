from django.shortcuts import render
from django.views import View
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage


# ------------------------------------------------------------------
# Keep your original class-based views exactly as they were.
# If any of these need extra logic, add it inside the class bodies.
# ------------------------------------------------------------------

class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')


class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html', {'success': False})

    def post(self, request):
        name    = request.POST.get('name', '').strip()
        email   = request.POST.get('email', '').strip()
        topic   = request.POST.get('topic', '').strip()
        message = request.POST.get('message', '').strip()

        # Save to database -- shows up in /admin
        ContactMessage.objects.create(
            name=name,
            email=email,
            topic=topic,
            message=message,
        )

        # Send email directly to your inbox
        send_mail(
            subject=f"[TerraBloom] New message: {topic}",
            message=(
                f"New contact form submission.\n\n"
                f"Name:    {name}\n"
                f"Email:   {email}\n"
                f"Topic:   {topic}\n\n"
                f"Message:\n{message}\n\n"
                f"---\nSent via TerraBloom Contact Form"
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.CONTACT_RECIPIENT_EMAIL],
            fail_silently=False,
        )

        return render(request, 'contact.html', {'success': True})


class ConsumerOrderView(View):
    def get(self, request):
        return render(request, 'consumer_order.html')

    def post(self, request):
        # Add your consumer order logic here
        return render(request, 'consumer_order.html')


class FarmerUploadView(View):
    def get(self, request):
        return render(request, 'form upload.html')

    def post(self, request):
        # Add your farmer upload logic here
        return render(request, 'form upload.html')


class DashboardView(View):
    def get(self, request):
        return render(request, 'dashboard.html')
