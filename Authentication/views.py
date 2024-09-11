from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

from Authentication.forms import MyUserCreationForm


# Create your views here.

class SignUpView(FormView):
    template_name = 'registration/signup.html'
    form_class = MyUserCreationForm
    success_url = reverse_lazy('Authentication:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



class Test(View):
    def get(self, request):
        return HttpResponse('test działania autoryzacji')