from django.shortcuts import render, get_object_or_404

from .models import *
from .forms import NewComment


# Create your views here.
def index(request):
    context = {
        'title': 'الصفحة الرئيسية',
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/index.html', context)

def about(request):
    context = {
        'title': 'من أنا',
    }
    return render(request, 'blog/about.html', context)

def post_detail(requset, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.filter(active=True)

    if requset.method == 'POST':
        comment_form = NewComment(data=requset.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            comment_form = NewComment()
    else:
        comment_form = NewComment()

    context = {
        'title': post.title,
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(requset, 'blog/detail.html', context)
