from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


#Thông tin Users
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #img
    address = models.CharField(max_length=100, help_text="Địa chỉ")
    email = models.BooleanField(default=False)
    created_on = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.user.username}'s Profile"


