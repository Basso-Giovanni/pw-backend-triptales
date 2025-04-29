from rest_framework import serializers
from .models import Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image', 'description', 'created_at', 'created_by', 'latitude', 'longitude']
        read_only_fields = ['created_at', 'created_by']
