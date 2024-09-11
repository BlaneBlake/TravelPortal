from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import FormView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from Authentication.forms import MyUserCreationForm
from TravelPortal.mixins.context_mixins import TextsMixin

# Create your views here.

class CustomLoginView(TextsMixin, LoginView):
    template_name = 'registration/login.html'

class SignUpView(TextsMixin, FormView):
    template_name = 'registration/signup.html'
    form_class = MyUserCreationForm
    success_url = reverse_lazy('Authentication:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UserProfileView(LoginRequiredMixin, TextsMixin, DetailView):
    model = User
    template_name = 'registration/user_profile.html'
    context_object_name = 'user_profile'

    def get_object(self, queryset=None):
        return self.request.user


class Test(View):
    def get(self, request):
        return HttpResponse('test działania autoryzacji')