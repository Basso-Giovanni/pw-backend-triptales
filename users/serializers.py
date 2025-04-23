from rest_framework import serializers
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'bio', 'avatar']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Verifica che 'username' sia presente nei dati
        if 'username' not in validated_data:
            raise serializers.ValidationError({"username": "Questo campo è obbligatorio"})

        # Crea l'utente
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            avatar=validated_data.get('avatar', None)
        )
        return user
