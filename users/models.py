from django.contrib.auth.models import AbstractUser
from django.db import models

"""
    Modello per l'utente. Deriva dalla classe AbstractUser di Django e aggiunge i campi bio e avatar.
"""
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'customuser'