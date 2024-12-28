from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Photo
from .widgets import MultiFileInput



class MultiPhotoUploadForm(forms.Form):
    images = forms.FileField(
        label=_("Upload Photos"),
        widget=MultiFileInput,
        required=False
    )

class ManagePhotoForm(forms.ModelForm):
    delete = forms.BooleanField(required=False, label=_("Delete this photo"))

    class Meta:
        model = Photo
        fields = ['delete']

class SelectMainPhotoForm(forms.Form):
    main_photo = forms.ModelChoiceField(
        queryset=None,
        label=_("Select Main Photo"),
        required=True
    )

    def __init__(self, *args, **kwargs):
        gallery = kwargs.pop('gallery', None)
        super().__init__(*args, **kwargs)
        if gallery:
            self.fields['main_photo'].queryset = gallery.photos.all()
