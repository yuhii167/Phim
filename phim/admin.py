from django.contrib import admin
from .models.Users import Profile
from .models.category_model import Category
from .models.movie_model import Movie
from .models.actor import Actor
from .models.ads_model import Ads

#Đăng kí profile ở Admin
class ProfileAdmin(admin.ModelAdmin):
    list_filter = ('user',)
    search_fields = ('user',)
    ordering = ['user',]

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Movie)
admin.site.register(Ads)

admin.site.register(Actor)




# Registers the category model at the admin backend.
admin.site.register(Category)