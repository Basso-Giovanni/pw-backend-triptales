from django.conf import settings
from django.db import models
from images.models import Image
from trips.models import TripGroup

#model del post
class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='created_posts',
        on_delete=models.SET_NULL,
        null=True
    )
    image = models.ForeignKey(
        Image,
        related_name='posts',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='liked_posts',
        blank=True
    )
    group = models.ForeignKey(
        TripGroup,
        related_name='posts',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()