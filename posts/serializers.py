from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'created_at', 'created_by', 'image', 'likes_count']

    def get_likes_count(self, obj):
        return obj.likes.count()
