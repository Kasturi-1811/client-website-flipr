from django.db import models
from core.utils import crop_image

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            crop_image(self.image.path)

    def __str__(self):
        return self.name
