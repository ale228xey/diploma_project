from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from main.forms import CommentFormForPost
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


# class PostDetail(DetailView):
#     model = Post
#     template_name = 'detail_post.html'
#     context_object_name = 'post'

class PostDetail(View):
    template_name = 'detail_post.html'
    comment_form = CommentFormForPost

    def get(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        context = {}
        context['post'] = post
        context['comments'] = post.comments.filter(status_comment=True)
        context['form'] = self.comment_form
        return render(request, template_name=self.template_name, context=context)


class ProjectDetail(DetailView):
    model = Project
    template_name = 'detail_project.html'
    context_object_name = 'project'
