from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display    = ('name', 'email', 'topic', 'sent_at')
    list_filter     = ('topic', 'sent_at')
    search_fields   = ('name', 'email', 'message')
    readonly_fields = ('name', 'email', 'topic', 'message', 'sent_at')
    ordering        = ('-sent_at',)

    def has_add_permission(self, request):
        # Messages should only arrive through the contact form
        return False
