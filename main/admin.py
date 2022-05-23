from django.contrib import admin

# Register your models here.
from main.models import Owner, Post

admin.site.register(Owner)
admin.site.register(Post)