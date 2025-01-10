from django.http import Http404
from django.views.generic import (
    TemplateView,
    CreateView,
    ListView,
    DetailView,
    UpdateView)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.forms import modelformset_factory
from django.conf import settings

from .models import Post
from .forms import PostForm

from Gallery.models import Gallery, Photo
from Gallery.forms import MultiPhotoUploadForm, ManagePhotoForm, SelectMainPhotoForm

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
            context['photo_form'] = MultiPhotoUploadForm(self.request.POST, self.request.FILES)

        else:
            context['photo_form'] = MultiPhotoUploadForm()

        # Add Google Maps API Key to the context
        context['GOOGLE_MAPS_API_KEY'] = settings.GOOGLE_MAPS_API_KEY

        return context

class PostEditView(TextsMixin, LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def get_queryset(self):
        # Umożliwia edycję tylko postów należących do aktualnie zalogowanego użytkownika
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)

    def get_object(self, queryset=None):
        # Pobieranie obiektu do edycji, jeśli użytkownik jest autorem
        obj = super().get_object(queryset)
        if obj.author != self.request.user:
            raise Http404("You are not the author of this post.")
        return obj

    def get_context_data(self, **kwargs):
        # Dodanie formsetu do kontekstu
        context = super().get_context_data(**kwargs)
        gallery = self.object.gallery

        if self.request.POST:
            context['photo_form'] = MultiPhotoUploadForm(self.request.POST, self.request.FILES)
            context['manage_photo_formset'] = self.get_manage_photo_formset(self.request.POST)

        else:
            context['photo_form'] = MultiPhotoUploadForm()
            context['manage_photo_formset'] = self.get_manage_photo_formset()

        context['photos'] = gallery.photos.all()

        # Add Google Maps API Key to the context
        context['GOOGLE_MAPS_API_KEY'] = settings.GOOGLE_MAPS_API_KEY

        return context

    def get_manage_photo_formset(self, post_data=None):
        gallery = self.object.gallery
        PhotoFormSet = modelformset_factory(
            Photo,
            form=ManagePhotoForm,
            extra=0
        )
        if post_data:
            return PhotoFormSet(post_data, queryset=gallery.photos.all())
        return PhotoFormSet(queryset=gallery.photos.all())


    def form_valid(self, form):
        # Zapisz formularz posta
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

        # Obsługa zarządzania istniejącymi zdjęciami
        manage_photo_formset = self.get_manage_photo_formset(self.request.POST)
        if manage_photo_formset.is_valid():
            for photo_form in manage_photo_formset:
                photo = photo_form.save(commit=False)
                if photo_form.cleaned_data.get('delete'):
                    photo.delete()
                else:
                    photo.save()

        # Sprawdzanie, czy zostało wybrane nowe zdjęcie główne
        main_photo_id = self.request.POST.get('photo')
        if main_photo_id:
            try:
                main_photo = Photo.objects.get(id=main_photo_id)
                main_photo = Photo.objects.get(id=main_photo_id)
                main_photo.is_main = True
                main_photo.save()  # Zapisz zmianę
            except Photo.DoesNotExist:
                pass

        return super().form_valid(form)


    def get_success_url(self):
        # Po zapisaniu, użytkownik zostaje przekierowany na stronę szczegółów posta
        return reverse_lazy('Blog:post_detail', kwargs={'pk': self.object.pk})

class PostListView(TextsMixin, ListView):
    model = Post
    template_name = 'blog/posts.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

class UserPostListView(TextsMixin, LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        # Pobiera tylko posty należące do zalogowanego użytkownika
        return Post.objects.filter(author=self.request.user).order_by('-created_at')

    def calculate_completion_percentage(self, post):
        total_fields = 4
        filled_fields = sum(bool(getattr(post, field)) for field in [
            'title',
            'content',
            'estimated_time',
            'location_url'
            # dwa poniższe to pola w innej tabeli
            # 'gallery',
            # 'tags',
        ])
        return int((filled_fields / total_fields) * 100)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for post in context['posts']:
            post.completion_percentage = self.calculate_completion_percentage(post)
        return context

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

        context['thumbnails'] = [photo.thumbnail.url for photo in context['photos']]

        return context
