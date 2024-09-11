from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


import json

with open('lang/lang_pl.json', 'r', encoding='utf-8') as file:
    texts = json.load(file)

# Create your views here.

class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'blog/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['texts'] = texts
        return context

class Test(View):
    def get(self, request):
        return HttpResponse('test działania blogu')