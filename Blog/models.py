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

    main_image = models.ImageField(upload_to='posts/main_images/', null=True, blank=True)
    tags = TaggableManager()
    location_url = models.URLField(max_length=500, null=True, blank=True)
    place_name = models.CharField(max_length=200, null=True, blank=True)
    estimated_time = models.DurationField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.title

class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='posts/images/')

    def __str__(self):
        return f'Image for post: {self.post.title}'