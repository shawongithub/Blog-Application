from django import forms
from App_Blog.models import Comment, Blog


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('comment',)