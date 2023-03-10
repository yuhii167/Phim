from django.db import models
from django.utils import timezone

from phim.models.movie_model import Movie

#Ung dung thu 3
from cloudinary.models import CloudinaryField

#model dien vien
class Actor(models.Model):

    #Gioi tinh
    MALE = "Nam"
    FAMELE = "Nữ"
    LGBT = "LGBT"

    #Lua Chon
    STATUS_CHOICES = (
        (MALE, 'Nam'),
        (FAMELE, 'Nữ'),
        (LGBT, 'LGBT'),
    )

    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10, choices=STATUS_CHOICES, default='')
    info = models.TextField()
    birth = models.DateField()
    flyer = CloudinaryField('Fyler')
    movies = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='moives')

    class Meta:
        unique_together = ("name",)
        verbose_name = 'actor'
        verbose_name_plural = 'actores'

    def __str__(self):
        return self.name