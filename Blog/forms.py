from datetime import timedelta

from django import forms
from .models import Post, PostImage
from taggit.forms import TagWidget

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
            'estimated_time': forms.TextInput(attrs={'placeholder': 'Enter time in HH:MM format'}),
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
                    raise forms.ValidationError('Enter a valid time in HH:MM format.')

            return estimated_time

class PostImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ['image']