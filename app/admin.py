from django.contrib import admin
from app.models import *


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'active']
