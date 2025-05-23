from rest_framework import serializers
from trips.models import TripGroup, Badge

#serializzatore per i gruppi
class TripGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripGroup
        fields = ['id', 'name', 'description', 'created_at', 'created_by', 'members']
        read_only_fields = ['id', 'created_at', 'created_by', 'members']

#serializzatore per i badge
class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = ['name', 'description']
