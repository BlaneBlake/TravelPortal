from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.forms import modelformset_factory
from django.conf import settings

from .models import Post, PostImage
from .forms import PostForm, PostImageForm
from TravelPortal.mixins.context_mixins import TextsMixin


from django.utils.translation import get_language

# Create your views here.

class HomePageView(TextsMixin, TemplateView):
    template_name = 'blog/home.html'

# Translation tests
#     -----------------------
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['LANGUAGE_CODE'] = get_language()  # Bieżący język
        context['LANGUAGES'] = settings.LANGUAGES  # Dostępne języki
        return context
#     -----------------------


class Test(TextsMixin, TemplateView):
    template_name = 'test.html'

class PostCreateView(TextsMixin, LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('Blog:post_list')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        post = form.save()

        images_formset = self.get_images_formset()
        if images_formset.is_valid():
            images = images_formset.save(commit=False)
            for image in images:
                image.post = post
                image.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        if self.request.POST:
            data['images_formset'] = self.get_images_formset()
        else:
            data['images_formset'] = self.get_images_formset(empty=True)

        # Add Google Maps API Key to the context
        data['GOOGLE_MAPS_API_KEY'] = settings.GOOGLE_MAPS_API_KEY

        return data

    def get_images_formset(self, empty=False):
        PostImageFormSet = modelformset_factory(PostImage, form=PostImageForm, extra=2)
        if empty:
            return PostImageFormSet(queryset=PostImage.objects.none())
        return PostImageFormSet(self.request.POST, self.request.FILES)

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
        context['images'] = self.object.images.all()
        context['tags'] = self.object.tags.all()
        return context
