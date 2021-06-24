from django.db import models
from base.models import BaseImage


class Image(BaseImage):
    scale = models.FloatField(blank=True, null=True)

