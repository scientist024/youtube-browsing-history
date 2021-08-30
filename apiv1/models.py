from django.db import models


class Streamer(models.Model):
    name = models.CharField(max_length=50)
    channel = models.URLField()

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    detail = models.TextField()
    fun = models.PositiveIntegerField(default=5)
    watched_date = models.DateField()
    streamers = models.ManyToManyField(Streamer)

    def __str__(self):
        return self.title
