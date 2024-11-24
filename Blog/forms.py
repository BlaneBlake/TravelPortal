from datetime import timedelta

from django import forms
from .models import Post, PostImage
from taggit.forms import TagWidget

from TravelPortal.settings import TEXTS

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title',
                  'content',
                  'main_image',
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
            'estimated_time': forms.TextInput(attrs={'placeholder': TEXTS["form"]["post"]["enterEstimatedTime"]}),
        }
        labels = {
            'title': TEXTS["form"]["post"]["title"],
            'content': TEXTS["form"]["post"]["content"],
            'main_image': TEXTS["form"]["post"]["mainImage"],
            'tags': TEXTS["form"]["post"]["tags"],
            'estimated_time': TEXTS["form"]["post"]["estimatedTime"],
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
                    raise forms.ValidationError(TEXTS["form"]["post"]["estimatedTimeValidationError"])

            return estimated_time

class PostImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ['image']
        labels = {
            'image': TEXTS["form"]["post"]["photo"],
        }