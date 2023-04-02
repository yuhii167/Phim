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

#Search
from taggit.models import Tag
from phim.models.category_model import Category
from django.db.models import Count

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
    country = models.CharField(max_length=100)
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
        tags = filters.get('tags', None)
        release_year = filters.get('release_year', None)

        qs = Movie.objects.all()

        if query:
            query_lookups = (Q(title__icontains=query) | Q(description__icontains=query) | Q(tags__name__icontains=query))
            qs = qs.filter(query_lookups).distinct()

        if category:
            qs = qs.filter(category__name__icontains=category)

        if tags:
            qs = qs.filter(tags__name__in=tags)

        if release_year:
            qs = qs.filter(release_date__year=release_year)

        return qs

    @staticmethod
    def get_filters(request):
        filters = {}
        query = request.GET.get('query')
        category = request.GET.get('category')
        tags = request.GET.getlist('tags')
        release_year = request.GET.get('release_year')

        if query:
            filters['query'] = query.strip()

        if category:
            filters['category'] = category.strip()

        if tags:
            filters['tags'] = [tag.strip() for tag in tags if tag.strip()]

        if release_year:
            filters['release_year'] = release_year.strip()

        return filters

    @staticmethod
    def get_categories():
        return Category.objects.all()

    @staticmethod
    def get_tags():
        return Tag.objects.all()

    @staticmethod
    def get_release_years():
        return [year for year in range(timezone.now().year, 1900, -1)]
    
    @staticmethod
    def get_countries():
        return Movie.objects.values('country').annotate(count=Count('country')).order_by('-count')

