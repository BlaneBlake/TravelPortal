from django.db import models
from Blog.models import Post
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


# Create your models here.

def user_post_photo_path(instance, filename):
    user_id = instance.gallery.post.author.id
    post_id = instance.gallery.post.id
    
    return f'users/{user_id}/posts/{post_id}/photos/{filename}'

class Gallery(models.Model):
    post = models.OneToOneField(Post, related_name='gallery', on_delete=models.CASCADE)  # Jedna galeria przypisana do jednego posta
    title = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title or f"Gallery for {self.post.title}"

class Photo(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='photos', on_delete=models.CASCADE)  # Zdjęcia w galerii
    image = models.ImageField(upload_to=user_post_photo_path)
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.caption or f"Photo in {self.gallery.title}"