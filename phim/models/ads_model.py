from django.db import models
#
from cloudinary.models import CloudinaryField

class Ads (models.Model):

    name = models.CharField(max_length=100)
    img = CloudinaryField('img')
    
    def __str__(self):
        return self.name