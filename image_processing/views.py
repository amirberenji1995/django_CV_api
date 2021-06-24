from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from image_processing.serializers import ImageSerializer, ImageScalerSerializer
from image_processing.models import Image
from CV_Scripts.image_grayer import image_grayer
from CV_Scripts.image_scaler import image_scaler
from django.conf import settings


# add stands for the address of the parent Django folder of the project
add = str(settings.BASE_DIR)

class ImageGrayerView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, format = None):
        file_serializer = ImageSerializer(data = request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            image = image_grayer(add, file_serializer.data['original'])
            File = Image.objects.latest('uploaded_at')
            File.processed = image
            File.save()
            File = Image.objects.latest('uploaded_at')
            result = ImageSerializer(File)
            return Response(result.data, status = status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImageScalerView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, format = None):
        file_serializer = ImageScalerSerializer(data = request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            image = image_scaler(add, file_serializer.data['original'], file_serializer.data['scale'])
            File = Image.objects.latest('uploaded_at')
            File.processed = image
            File.save()
            File = Image.objects.latest('uploaded_at')
            result = ImageScalerSerializer(File)
            return Response(result.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


