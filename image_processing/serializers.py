from rest_framework import serializers
from image_processing.models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('original', 'description', 'uploaded_at', 'processed')


class ImageScalerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('original', 'description', 'uploaded_at', 'processed', 'scale')

        extra_kwargs = {'scale': {'required': True}}

class ImageResizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('original', 'description', 'uploaded_at', 'processed', 'width', 'height')

        extra_kwargs = {'width': {'required': True}, 'height': {'required': True}}
