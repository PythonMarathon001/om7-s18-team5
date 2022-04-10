from rest_framework import serializers
from .models import *


class OrderSerializer(serializers.ModelSerializer):
    # user = serializers.SlugRelatedField(
    #     slug_field='last_name', queryset=CustomUser.objects)
    # book = serializers.SlugRelatedField(
    #     slug_field='name', queryset=Book.objects)

    class Meta:
        model = Order
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
