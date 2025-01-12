from django.contrib import admin
from .models import Gallery, Photo

# Register your models here.


# W panelu administracyjnym będziesz mógł edytować galerię i dodawać zdjęcia bezpośrednio w powiązaniu z postem.

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1  # Liczba pustych formularzy zdjęć

class GalleryAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]

admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Photo)