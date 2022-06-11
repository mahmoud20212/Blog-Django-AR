from django import forms
from .models import Comment, Post

class NewComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']

class PostCreateForm(forms.ModelForm):
    title = forms.CharField(label='عنوان التدوينة', help_text='العنوان يجب ألا يزيد عن 100 حرف')
    content = forms.CharField(label='نص التدوينة', widget=forms.Textarea())
    class Meta:
        model = Post
        fields = ['title', 'content']