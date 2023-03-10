from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

#model profile
from .models.Users import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *kwangs):
    if created:
        Profile.objects.create(user=instance)

#Tao ho so gia khi tao tai khoan
@receiver(post_save, sender=User)
def save_profile(sender,instance, **kwangs):
    instance.profile.save()