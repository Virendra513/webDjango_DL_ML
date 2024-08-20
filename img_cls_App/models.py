from django.db import models

# Create your models here.
from cloudinary.models import CloudinaryField

# Create your models here.
class MyModel(models.Model):
    image = CloudinaryField('image')

    def __str__(self):
        return f"Image: {self.image.url}"
