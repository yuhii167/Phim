from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Category(models.Model):

    name = models.CharField(max_length=100, null=False, blank=False)
    slug = models.SlugField()
 
    class Meta:
        unique_together = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('phim:category_movies',
                       kwargs={'slug': self.slug})
    