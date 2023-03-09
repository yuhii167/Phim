from django.db import models
import uuid
from phim.models.category_model import Category
from django.utils.text import slugify
from django.utils import timezone

#Ung dung T3
from taggit.managers import TaggableManager

#model phim
class Movie(models.Model):

    #trang thai phim
    DRAFTED = "RAW"
    FULLHD = "FULLHD"

    #lua chon
    STATUS_CHOICES = (
        (DRAFTED, 'RAW'),
        (FULLHD, 'FULLHD'),
    )

    title:str=models.CharField(max_length=225)
    description:str=models.TextField()
    created =models.DateTimeField(auto_now_add=True)
    uuid=models.UUIDField(default=uuid.uuid4,unique=True)
    slug = models.SlugField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                              default='RAW')
    views = models.PositiveIntegerField(default=0)
   
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='Category')
    videos=models.ManyToManyField('Video')
    date_published = models.DateTimeField(null=True, blank=True,
                                          default=timezone.now)
    flyer=models.ImageField(upload_to='flyers',blank=True,null=True)
    class Meta:
        unique_together = ("title",)
        ordering = ('-date_published',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Movie, self).save(*args, **kwargs)

    
class Video(models.Model):
    title:str = models.CharField(max_length=225,blank=True,null=True)
    file=models.FileField(upload_to='movies')