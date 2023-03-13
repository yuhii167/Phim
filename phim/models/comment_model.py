from django.db import models
from django.utils import timezone

from phim.models.Users import User

class Comment(models.Model):

    name = models.ForeignKey(User, on_detele=models.CASCADE, related_name='comments')
    comment = models.TextField(null = False, blank=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Nhận xét của {self.name}"