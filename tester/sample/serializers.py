from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed, ValidationError
import jwt
from django.conf import settings
from .models import User
\

class UserSerializer(serializers.ModelSerializer):
    """
            Creates a User
    """

    class Meta:
        model = User 
        fields = ['name','phone']
    
    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self,instance,validated_data):
        instance.phone = validated_data.get('phone',instance.phone)
        instance.name = validated_data.get('name',instance.name)
        instance.save()
        return instance
    
    
    

