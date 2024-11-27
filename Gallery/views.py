from django.shortcuts import render
from django.views.generic import TemplateView
from TravelPortal.mixins.context_mixins import TextsMixin
from django.utils.translation import gettext_lazy as _


# Create your views here.

class Test(TextsMixin, TemplateView):
    template_name = 'test.html'

    def get_context_data(self, **kwargs):
        # Pobranie domyślnego kontekstu
        context = super().get_context_data(**kwargs)
        # Dodanie własnych danych do kontekstu
        context['test_type'] = _("Gallery")
        return context
