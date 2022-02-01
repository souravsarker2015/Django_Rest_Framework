from django.db import models


# class StreamingPlatform(models.Model):
#     name = models.CharField(max_length=50)
#     about = models.CharField(max_length=250)
#     website_link = models.URLField(max_length=150)
#
#
# class WatchList(models.Model):




class Movie(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
