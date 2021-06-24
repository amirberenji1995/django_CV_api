from django.db import models
from base.models import BaseImage


class Image(BaseImage):
    scale = models.FloatField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
