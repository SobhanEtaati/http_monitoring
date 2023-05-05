from rest_framework import serializers
from .models import CustomUsers, URLs

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUsers
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUsers.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
    

class URLSerializer(serializers.Serializer):
    model = URLs
    url = serializers.URLField()
    status_code = serializers.IntegerField(max_length=3)
