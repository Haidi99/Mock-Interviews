from rest_framework import serializers
from .models import User, Subscribe
from django.contrib.auth.models import User


# class PersonSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = (
#         'first_name', 
#         'last_name', 
#         'email', 
#         'password', 
#         'phone'
#         )

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user

class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = '__all__'