from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class StreamingPlatform(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=250)
    website_link = models.URLField(max_length=150)

    def __str__(self):
        return self.name


class WatchList(models.Model):
    title = models.CharField(max_length=150)
    story_line = models.CharField(max_length=150)
    platform = models.ForeignKey(StreamingPlatform, on_delete=models.CASCADE, related_name='watchlist')  # related name is important
    active = models.BooleanField(default=True)
    avg_rating = models.FloatField(default=0.0)
    num_rating = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=200, null=True)
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name='reviews')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.rating)
# class Movie(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.CharField(max_length=200)
#     active = models.BooleanField(default=True)
#
#     def __str__(self):
#         return self.name
