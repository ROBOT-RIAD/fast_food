from rest_framework import serializers
from .import models

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Item
        fields ='__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'