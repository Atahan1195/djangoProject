from django.db import models


class Gallery(models.Model):
    name = models.CharField(max_length=50, unique=True)
    is_visible = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='gallery', blank=True)
    position = models.PositiveSmallIntegerField(default=1)

