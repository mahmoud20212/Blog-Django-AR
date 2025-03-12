from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Comment, Post

class NewComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']

class PostCreateForm(forms.ModelForm):
    title = forms.CharField(label=_('title'), help_text=_('title should not be more than 100 characters.'))
    content = forms.CharField(label=_('content'), widget=forms.Textarea())

    class Meta:
        model = Post
        fields = ['title', 'content']