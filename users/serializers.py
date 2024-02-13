from datetime import datetime
from rest_framework import serializers
from .models import CustomUser

class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['name', 'email', "id"]

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        
        instance.save()
        return instance