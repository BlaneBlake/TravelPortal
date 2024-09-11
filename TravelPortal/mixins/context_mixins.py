from django.conf import settings


class TextsMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['texts'] = settings.TEXTS
        return context