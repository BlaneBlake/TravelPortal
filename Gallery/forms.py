from django import forms
from .models import Gallery, Photo
from django.utils.translation import gettext_lazy as _


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['title']
        labels = {
            'title': _('Gallery title'),
        }

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'caption']
        labels = {
            'image': _('Photo'),
            'caption': _('Caption'),
        }
