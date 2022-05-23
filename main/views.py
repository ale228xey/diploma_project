from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView, ListView

from main.models import Post


class MainPage(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'