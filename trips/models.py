from django.db import models
from django.conf import settings
from users.models import CustomUser

#model del gruppo
class TripGroup(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='created_groups', on_delete=models.CASCADE
    )
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='trip_groups', blank=True
    )

    def __str__(self):
        return self.name

#model del badge
class Badge(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

#model per il badge dell'utente (un utente può avere solo un badge per ogni gruppo)
class UserGroupBadge(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    group = models.ForeignKey(TripGroup, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    date_awarded = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'group')

    def __str__(self):
        return f"{self.user.username} - {self.badge.name} in {self.group.name}"
