from django import forms
from django.utils.translation import gettext_lazy as _
from .widgets import MultiFileInput



class MultiPhotoUploadForm(forms.Form):
    images = forms.FileField(
        label=_("Upload Photos"),
        widget=MultiFileInput,
        required=False
    )