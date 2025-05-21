from django.conf import settings
from django.db import models

#model dei commenti
class Comment(models.Model):
    post = models.ForeignKey('posts.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} - {self.text[:30]}"
