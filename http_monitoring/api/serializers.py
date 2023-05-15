from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import ValidationError
from .models import User


class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=80)
    username = serializers.CharField(max_length=45)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        email_exists = User.objects.filter(email=attrs["email"]).exists()

        if email_exists:
            raise ValidationError("Email has already been used")

        return super().validate(attrs)


    #Overriding the Create method in ModelSerializer
    def create(self, validated_data):
        print('in serializer create method - 1')
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()

        print('---------------------------------')
        print(type(validated_data))
        print('---------------------------------')
        print(validated_data)
        print('---------------------------------')
        print(type(user))
        print('---------------------------------')
        print('in serializer create method - 2')

        Token.objects.create(user=user)


        print('in serializer create method - 3')

        return user
        
        #user = CustomUsers.objects.create_user(
        #    email=validated_data['email'],
        #    username=validated_data['username'],
        #    password=validated_data['password']
        #)

