from django.db import models
from Blog.models import Post
from django.utils.translation import gettext_lazy as _
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


# Create your models here.

def user_post_photo_path(instance, filename):
    user_id = instance.gallery.post.author.id
    post_id = instance.gallery.post.id
    
    return f'users/{user_id}/posts/{post_id}/photos/{filename}'

class Gallery(models.Model):
    post = models.OneToOneField(Post, related_name='gallery', on_delete=models.CASCADE)

    def get_main_photo(self):
        return self.photos.filter(is_main=True).first() or self.photos.first()

    def __str__(self):
        return f"{_('Gallery')} {self.post.title}"

class Photo(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_post_photo_path)
    caption = models.CharField(max_length=200, blank=True)
    is_main = models.BooleanField(default=False)

    thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(100, 100)],  # Zmienia rozmiar na 100x100 px
        format='JPEG',
        options={'quality': 60}  # Możesz dostosować jakość miniatury
    )

    def save(self, *args, **kwargs):

        if self.is_main:
            Photo.objects.filter(gallery=self.gallery, is_main=True).update(is_main=False)
        else:
            if not self.gallery.photos.filter(is_main=True).exists():
                self.is_main = True
        super().save(*args, **kwargs)

    def __str__(self):
        return self.caption or f"{_('Photo in')} {self.gallery.post.title}"