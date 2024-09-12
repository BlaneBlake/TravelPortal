from django import forms
from .models import Post, PostImage
from taggit.forms import TagWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'main_image', 'tags', 'location_url', 'place_name', 'estimated_time']
        widgets = {
            'tags': TagWidget(),
        }

class PostImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ['image']