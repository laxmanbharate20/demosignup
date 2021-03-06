from rest_framework import serializers
from .models import RegisterModel
from django.contrib.auth.models import User
import requests
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source='user.email',required=True,validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(source='user.username',required=True,validators=[UniqueValidator(queryset=User.objects.all())])
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    password = serializers.CharField(source='user.password',write_only=True, required=True,validators = [validate_password])

    class Meta:
        """metadata of RegisterSerializer """
        model = RegisterModel
        fields = ('username', 'first_name', 'last_name','business_name','business_licn_no','phone_no','email','password')

    def create(self, validated_data):
        """create new records"""
        user_data = validated_data.pop('user')
        user = User.objects.create(username=user_data['username'],first_name=user_data['first_name'],last_name=user_data['last_name'],email=user_data['email'])
        user.set_password(user_data['password'])
        user.save()

        profile = RegisterModel.objects.create(user=user, **validated_data)
        return profile

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email')