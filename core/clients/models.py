from django.db import models
from core.utils import crop_image

class Client(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='clients/')

    def __str__(self):
        return self.name
