from rest_framework import serializers
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'bio', 'avatar']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        if 'username' not in validated_data:
            raise serializers.ValidationError({"username": "Questo campo è obbligatorio"})

        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            avatar=validated_data.get('avatar', None)
        )
        return user

    def update(self, instance, validated_data):
        # Gestione separata della password per assicurarne la cifratura
        password = validated_data.pop('password', None)

        # Aggiorna gli altri campi normalmente
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)

        instance.save()
        return instance

class PublicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'avatar']
