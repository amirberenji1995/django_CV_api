from django.urls import path
from .views import ImageGrayerView, ImageScalerView, ImageResizerView

urlpatterns = [
    path('grayer/', ImageGrayerView.as_view(), name='image-grayer'),
    path('scaler/', ImageScalerView.as_view(), name='image-scaler'),
    path('resizer/', ImageResizerView.as_view(), name='image-resizer'),
]
