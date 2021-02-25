from rest_framework import serializers
from face_detection.models import FaceImage


class FaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaceImage
        fields = ('original', 'description', 'uploaded_at', 'processed')

