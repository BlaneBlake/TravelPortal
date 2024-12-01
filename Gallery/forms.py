from django import forms
from .models import Gallery, Photo
from django.utils.translation import gettext_lazy as _


# class GalleryForm(forms.ModelForm):
#     class Meta:
#         model = Gallery
#         fields = ['gallery_title']
#         labels = {
#             'gallery_title': _('Gallery title'),
#         }

from django.forms.widgets import ClearableFileInput

class MultiFileInput(ClearableFileInput):
    allow_multiple_selected = True

    def __init__(self, attrs=None):
        if attrs is None:
            attrs = {}
        attrs['multiple'] = True
        super().__init__(attrs)


class MultiPhotoUploadForm(forms.Form):
    images = forms.FileField(
        label=_("Upload Photos"),
        widget=MultiFileInput,
        required=False
    )