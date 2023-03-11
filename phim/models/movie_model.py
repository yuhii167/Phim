from django.db import models
import uuid
from django.urls import reverse
from phim.models.category_model import Category
from django.utils.text import slugify
from django.utils import timezone


from phim.models.actor import Actor
#Ung dung T3
from taggit.managers import TaggableManager
from cloudinary.models import CloudinaryField

#model phim
class Movie(models.Model):

    #trang thai phim
    DRAFTED = "RAW"
    FULLHD = "FULLHD"
    COMINGSOON = "COMINGSOON"

    #lua chon
    STATUS_CHOICES = (
        (DRAFTED, 'RAW'),
        (FULLHD, 'FULLHD'),
        (COMINGSOON,'COMINGSOON'),
    )

    title:str=models.CharField(max_length=225)
    description:str=models.TextField()
    created =models.DateTimeField(auto_now_add=True)
    uuid=models.UUIDField(default=uuid.uuid4,unique=True)
    contry = models.CharField(max_length=100)
    slug = models.SlugField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                              default='RAW')
    views = models.PositiveIntegerField(default=0)
    time = models.CharField(max_length=100)
    
    trailer = models.CharField(max_length=400)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='movies')
    movies = models.CharField(max_length=500)
    date_published = models.DateTimeField(null=True, blank=True,
                                          default=timezone.now)
    DN = models.CharField(max_length=4)
    flyer=CloudinaryField('img')
    stars = models.ManyToManyField(Actor, related_name='movies')

    class Meta:
        unique_together = ("title",)
        verbose_name = 'movie'
        verbose_name_plural = 'movies'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Movie, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('phim:movies',
                       kwargs={'slug': self.slug})
    
