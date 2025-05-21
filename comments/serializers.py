from rest_framework import serializers
from .models import Comment

#serializzatore dei commenti
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'text', 'created_at']
        read_only_fields = ['author', 'created_at', 'post']
