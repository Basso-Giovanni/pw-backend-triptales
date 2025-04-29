from django.conf import settings
from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='uploads/')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='created_images', on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return f"Image {self.id} by {self.created_by}"
