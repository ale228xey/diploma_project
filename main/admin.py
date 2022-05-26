from django.contrib import admin

# Register your models here.
from main.models import Owner, Post, Project, CommentForPost

admin.site.register(Owner)
admin.site.register(Post)
admin.site.register(Project)
admin.site.register(CommentForPost)
