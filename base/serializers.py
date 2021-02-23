from rest_framework import serializers
from models import BaseImage


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseImage
        fields = ('original', 'description', 'uploaded_at', 'processed')

