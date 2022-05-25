from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from main.models import Post, Project


class MainPage(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    paginate_by = 2


class ProjectPage(ListView):
    model = Project
    template_name = 'work.html'
    context_object_name = 'projects'


class AboutPage(TemplateView):
    template_name = 'about.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'detail_post.html'
    context_object_name = 'post'


class ProjectDetail(DetailView):
    model = Project
    template_name = 'detail_project.html'
    context_object_name = 'project'
