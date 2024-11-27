from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.forms import modelformset_factory
from django.conf import settings

from .models import Post
from .forms import PostForm

from Gallery.models import Gallery, Photo
from Gallery.forms import GalleryForm, PhotoForm

from TravelPortal.mixins.context_mixins import TextsMixin


from django.utils.translation import get_language
from django.utils.translation import gettext_lazy as _

# Create your views here.

class Test(TextsMixin, TemplateView):
    template_name = 'test.html'
    def get_context_data(self, **kwargs):
        # Pobranie domyślnego kontekstu
        context = super().get_context_data(**kwargs)
        # Dodanie własnych danych do kontekstu
        context['test_type'] = _("Blog")
        return context

class HomePageView(TextsMixin, TemplateView):
    template_name = 'blog/home.html'

class PostCreateView(TextsMixin, LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('Blog:post_list')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        post = form.save()

        # Tworzenie galerii dla posta
        gallery_form = GalleryForm(self.request.POST)
        if gallery_form.is_valid():
            gallery = gallery_form.save(commit=False)
            gallery.post = post
            gallery.save()

            # Obsługa zdjęć
            photos_formset = self.get_photos_formset()
            if photos_formset.is_valid():
                photos = photos_formset.save(commit=False)
                for photo in photos:
                    photo.gallery = gallery
                    photo.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.POST:
            context['gallery_form'] = GalleryForm(self.request.POST)
            context['photos_formset'] = self.get_photos_formset()
        else:
            context['gallery_form'] = GalleryForm()
            context['photos_formset'] = self.get_photos_formset(empty=True)

        # Add Google Maps API Key to the context
        context['GOOGLE_MAPS_API_KEY'] = settings.GOOGLE_MAPS_API_KEY

        return context

    def get_photos_formset(self, empty=False):
        PhotoFormSet = modelformset_factory(Photo, form=PhotoForm, extra=2)
        if empty:
            return PhotoFormSet(queryset=Photo.objects.none())
        return PhotoFormSet(self.request.POST, self.request.FILES)

class PostListView(TextsMixin, ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

class PostDetailView(TextsMixin, DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = self.object.tags.all()

        gallery = getattr(self.object, 'gallery', None)
        if gallery:
            context['gallery'] = gallery
            context['photos'] = gallery.photos.all()
        else:
            context['gallery'] = None
            context['photos'] = []

        return context
