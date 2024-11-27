from datetime import timedelta

from django import forms
from .models import Post
from taggit.forms import TagWidget

from TravelPortal.settings import TEXTS
from django.utils.translation import gettext_lazy as _

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title',
                  'content',
                  'tags',
                  'location_url',
                  # 'place_name',
                  'estimated_time',
                  'latitude',
                  'longitude']
        widgets = {
            'tags': TagWidget(),
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
            'location_url': forms.HiddenInput(),
            'estimated_time': forms.TextInput(attrs={'placeholder': _('Time in HH:MM format')}),
        }
        labels = {
            'title': _('Title'),
            'content': _('Content'),
            'tags': _('tags'),
            'estimated_time': _('Estimated time'),
        }

        def clean_estimated_time(self):
            # Pobranie wartości z formularza
            estimated_time = self.cleaned_data['estimated_time']

            if estimated_time:
                # Sprawdzenie poprawności formatu HH:MM
                try:
                    hours, minutes = map(int, estimated_time.split(':'))
                    return timedelta(hours=hours, minutes=minutes)
                except ValueError:
                    raise forms.ValidationError(_('Correct the format to HH:MM'))

            return estimated_time
