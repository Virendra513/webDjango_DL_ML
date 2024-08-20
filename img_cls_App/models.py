from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class MyModel(models.Model):
    image = models.ImageField()

    # def __str__(self):
    #     return f"Image: {self.image.url}"

