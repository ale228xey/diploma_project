from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=70)
    img = models.ImageField(upload_to='img/avatar', default=True)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Post(models.Model):
    author = models.ForeignKey(Owner, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=450)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Пост {self.author}'


class Project(models.Model):
    COMPLEXITY_CHOICES = [
        ('EZ', 'easy'),
        ('NO', 'normal'),
        ('HA', 'hard'),
    ]
    developer = models.ForeignKey(Owner, on_delete=models.CASCADE)
    project_url = models.CharField(max_length=150)
    about_project = models.TextField(max_length=400)
    complexity = models.CharField(max_length=2, choices=COMPLEXITY_CHOICES, blank=True)
    img_project = models.ImageField(upload_to='img/project', default=True)
