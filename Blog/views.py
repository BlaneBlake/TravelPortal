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
from Gallery.forms import MultiPhotoUploadForm

from TravelPortal.mixins.context_mixins import TextsMixin

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

        # Tworzenie galerii dla posta (lub jej pobranie, jeśli istnieje)
        gallery, _ = Gallery.objects.get_or_create(post=post)

        # Obsługa formularza przesyłania zdjęć
        photo_form = MultiPhotoUploadForm(self.request.FILES)
        if photo_form.is_valid():
            images = self.request.FILES.getlist('images')  # Pobranie wszystkich przesłanych plików
            for image in images:
                Photo.objects.create(gallery=gallery, image=image)

        else:
            print(f"Photo form errors: {photo_form.errors}")

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.POST:
            # context['gallery_form'] = GalleryForm(self.request.POST)
            context['photo_form'] = MultiPhotoUploadForm(self.request.POST, self.request.FILES)

        else:
            # context['gallery_form'] = GalleryForm()
            context['photo_form'] = MultiPhotoUploadForm()

        # Add Google Maps API Key to the context
        context['GOOGLE_MAPS_API_KEY'] = settings.GOOGLE_MAPS_API_KEY

        return context

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
            context['main_image'] = gallery.photos.filter(is_main=True).first() or gallery.photos.first()
        else:
            context['gallery'] = None
            context['photos'] = []
            context['main_image'] = None

        return context
