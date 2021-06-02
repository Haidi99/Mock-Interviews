from rest_framework import serializers
from .models import User, Subscribe

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
        'first_name', 
        'last_name', 
        'email', 
        'password', 
        'phone'
        )

class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = '__all__'