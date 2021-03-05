from django.urls import path
from .views import ImageGrayerView

urlpatterns = [
    path('grayer/', ImageGrayerView.as_view(), name='image-grayer'),
]
