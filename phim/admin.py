from django.contrib import admin
from .models.Users import Profile

#Đăng kí profile ở Admin
class ProfileAdmin(admin.ModelAdmin):
    list_filter = ('user',)
    search_fields = ('user',)
    ordering = ['user',]

admin.site.register(Profile, ProfileAdmin)
