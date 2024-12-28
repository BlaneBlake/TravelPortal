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
            'estimated_time': forms.Select(choices=[(timedelta(hours = i), f"{i} {_('hours')}") for i in range(1, 25)]),
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Ustawienie ukrytych pól jako opcjonalnych
        self.fields['location_url'].required = False
        self.fields['latitude'].required = False
        self.fields['longitude'].required = False
    #
    #     # Wymuszamy, żeby nie wysyłały błędów walidacji przy pustych polach
    #     self.fields['location_url'].empty_value = ''
    #     self.fields['latitude'].empty_value = None
    #     self.fields['longitude'].empty_value = None