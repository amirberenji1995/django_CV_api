from django.db import models


class BaseImage(models.Model):
    original = models.ImageField(blank=False, null=False)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.ImageField(blank=True)

    class Meta:
        abstract = True
