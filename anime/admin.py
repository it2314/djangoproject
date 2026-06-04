from django.contrib import admin
from django.contrib.auth.models import User
from .models import Anime, Studio, Theme, UserRating

class UserRatingAdmin(admin.ModelAdmin):
    list_display = ['user', 'anime', 'rating', 'text']
    list_filter = ['anime', 'rating', 'user']
    search_fields = ['user__username', 'anime__name', 'text']
    ordering = ['-id']

admin.site.register(Anime)
admin.site.register(Studio)
admin.site.register(Theme)
admin.site.register(UserRating, UserRatingAdmin)


