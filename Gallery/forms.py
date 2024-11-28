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
        fields = ['image', 'caption', 'is_main']
        labels = {
            'image': _('Photo'),
            'caption': _('Caption'),
            'is_main': _('Main image'),
        }

# class MultiPhotoUploadForm(forms.Form):
#     images = forms.FileField(
#         label=_("Upload Photos"),
#         widget=forms.FileInput(attrs={'multiple': True}),
#         required=False
#     )