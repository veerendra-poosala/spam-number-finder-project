from rest_framework import serializers 
from .models import RegisterUserModel 


class RegisterUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = RegisterUserModel 
        fields = '__all__'