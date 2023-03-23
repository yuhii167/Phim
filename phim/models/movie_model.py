from django.db import models
import uuid
from django.urls import reverse
from phim.models.category_model import Category
from django.utils.text import slugify
from django.utils import timezone
from django.db.models import Q


from phim.models.actor import Actor
#Ung dung T3
from taggit.managers import TaggableManager
from cloudinary.models import CloudinaryField
from taggit.managers import TaggableManager

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
    title_el =models.CharField(max_length=250)
    rating = models.CharField(max_length=10)
    description:str=models.TextField()
    created =models.DateTimeField(auto_now_add=True)
    uuid=models.UUIDField(default=uuid.uuid4,unique=True)
    contry = models.CharField(max_length=100)
    slug = models.SlugField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                              default='FULLHD')
    views = models.PositiveIntegerField(default=0)
    time = models.CharField(max_length=100)
 
    
    trailer = models.CharField(max_length=400)
    category = models.ManyToManyField(Category,
                                 related_name='movies')
    movies = models.CharField(max_length=500)
    date_published = models.DateTimeField(null=True, blank=True,
                                          default=timezone.now)
    year = models.CharField(max_length=4)
    flyer=CloudinaryField('img', transformation=[{'width': 400, 'height': 600, 'crop': 'fill'}])
    stars = models.ManyToManyField(Actor, related_name='movies')
    tags = TaggableManager(blank=True)

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
        return reverse('phim:phimdetail',
                       kwargs={'slug': self.slug})
    



class MovieSearch:
    @staticmethod
    def search_movies(filters):
        query = filters.get('query', None)
        category = filters.get('category', None)
        country = filters.get('country', None)
        year = filters.get('year', None)

        qs = Movie.objects.all()

        if query:
            query_lookups = (Q(title__icontains=query) | Q(description__icontains=query) | Q(category__name__icontains=query))
            qs = qs.filter(query_lookups).distinct()

        if category:
            qs = qs.filter(category__name__icontains=category)

        if country:
            qs = qs.filter(country__icontains=country)

        if year:
            qs = qs.filter(year__icontains=year)

        return qs
