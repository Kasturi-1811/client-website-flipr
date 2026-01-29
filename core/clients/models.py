from django.db import models
from core.utils import crop_image

class Client(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='clients/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            crop_image(self.image.path)

    def __str__(self):
        return self.name
