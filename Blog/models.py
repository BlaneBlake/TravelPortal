from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings

from taggit.managers import TaggableManager

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    tags = TaggableManager()
    location_url = models.URLField(max_length=500, null=True, blank=True)
    place_name = models.CharField(max_length=200, null=True, blank=True)
    estimated_time = models.DurationField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def gallery(self):
        return getattr(self, 'gallery', None)
