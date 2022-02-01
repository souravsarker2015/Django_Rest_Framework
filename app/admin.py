from django.contrib import admin
from app.models import *


@admin.register(StreamingPlatform)
class StreamingPlatformAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'about', 'website_link']


@admin.register(WatchList)
class WatchListAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'story_line', 'active', 'created']

# @admin.register(Movie)
# class MovieAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name', 'description', 'active']
