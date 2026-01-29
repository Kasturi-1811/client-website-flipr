from django.db import models

class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
