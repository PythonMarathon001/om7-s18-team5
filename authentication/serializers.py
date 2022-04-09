from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
