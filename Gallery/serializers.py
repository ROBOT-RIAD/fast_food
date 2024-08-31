from rest_framework import serializers
from .import models

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Gallery
        fields ='__all__'