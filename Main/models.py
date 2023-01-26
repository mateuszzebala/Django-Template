import os
import random
import string

from django.contrib.auth.models import User
from django.db import models

from Panel.config import register_model


def image_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{''.join(random.choices(string.ascii_lowercase, k=20))}.{ext}"
    return os.path.join('Media/video/', filename)

class Image(models.Model):
    image = models.ImageField(upload_to=image_name)

    def __str__(self):
        return f"{self.image.name}"

register_model(Image, ('id', 'image'))



