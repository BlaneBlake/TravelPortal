from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from TravelPortal.mixins.context_mixins import TextsMixin

# Create your views here.

class HomePageView(TextsMixin, TemplateView):
    template_name = 'blog/home.html'

class Test(TextsMixin, TemplateView):
    template_name = 'test.html'