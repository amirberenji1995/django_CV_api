from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from face_detection.serializers import FaceSerializer
from face_detection.models import FaceImage
from CV_Scripts.faceDetection import face_detector
from django.conf import settings


# add stands for the address of the parent Django folder of the project
add = str(settings.BASE_DIR)


class FaceDetectionView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, format = None):
        file_serializer = FaceSerializer(data = request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            image = face_detector(add, file_serializer.data['original'])
            File = FaceImage.objects.latest('uploaded_at')
            File.processed = image
            File.save()
            File = FaceImage.objects.latest('uploaded_at')
            result = FaceSerializer(File)
            return Response(result.data, status = status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)