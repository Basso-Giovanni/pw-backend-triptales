from rest_framework import serializers
from .models import Post
from trips.models import TripGroup

class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'description', 'created_at',
            'created_by', 'image', 'group', 'likes_count'
        ]
        read_only_fields = ['id', 'created_by', 'created_at', 'likes_count']

    def get_likes_count(self, obj):
        return obj.likes.count()

    def validate_group(self, value):
        if not TripGroup.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Il gruppo specificato non esiste.")
        return value