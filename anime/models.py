from django.db import models

class Studio(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Theme(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Anime(models.Model):
    STATUS_CHOICES = [
        ("airing", "Currently Airing"),
        ("finished", "Finished"),
        ("upcoming", "Upcoming"),
    ]

    TYPE_CHOICES = [
        ("tv", "TV"),
        ("movie", "Movie"),
        ("ova", "OVA"),
        ("ona", "ONA"),
        ("special", "Special"),
    ]

    name = models.CharField(max_length=200, unique=True)
    rating = models.FloatField(null=True, blank=True)
    image = models.ImageField(upload_to="anime_images/")
    synopsis = models.TextField()

    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    release_date = models.DateField(null=True, blank=True)
    episodes = models.IntegerField(null=True, blank=True)

    type = models.CharField(max_length=20, choices=TYPE_CHOICES)

    studios = models.ManyToManyField(Studio, blank=True)
    themes = models.ManyToManyField(Theme, blank=True)

    def __str__(self):
        return self.name