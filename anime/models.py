from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User

class Studio(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Studio"
        verbose_name_plural = "Studios"
        ordering = ['name']

class Theme(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Theme"
        verbose_name_plural = "Themes"
        ordering = ['name']
        
class UserRating(models.Model):
    anime = models.ForeignKey('Anime', related_name='user_ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
    text = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.anime.name} ({self.rating})"

    class Meta:
        verbose_name = "User Rating"
        verbose_name_plural = "User Ratings"
        ordering = ['anime', 'user']

class Anime(models.Model):
    STATUS_CHOICES = [
        ("Airing", "Currently Airing"),
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
    rating = models.FloatField(
        null=True, blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
    image = models.ImageField(upload_to="anime_images/")
    synopsis = models.TextField()

    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    release_date = models.DateField(null=True, blank=True)
    episodes = models.IntegerField(
        null=True, blank=True,
        validators=[MinValueValidator(1)]
    )

    type = models.CharField(max_length=20, choices=TYPE_CHOICES)

    studios = models.ManyToManyField(Studio, blank=True)
    themes = models.ManyToManyField(Theme, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Anime"
        verbose_name_plural = "Anime"
        ordering = ['name']
        
    def average_user_rating(self):
        ratings = self.user_ratings.all()
        if ratings.exists():
            return round(sum(r.rating for r in ratings) / ratings.count(), 2)
        return None