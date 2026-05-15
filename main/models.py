from django.db import models


class ContactMessage(models.Model):
    name    = models.CharField(max_length=200)
    email   = models.EmailField()
    topic   = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    sent_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering            = ['-sent_at']
        verbose_name        = 'Contact Message'
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return f"{self.name} - {self.topic} ({self.sent_at:%Y-%m-%d %H:%M})"
