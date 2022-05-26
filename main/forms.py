from django.forms import ModelForm

from main.models import CommentForPost


class CommentFormForPost(ModelForm):
    class Meta:
        model = CommentForPost
        fields = ('author_comment', 'content_comment')