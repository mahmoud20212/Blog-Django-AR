from django import template
from blog.models import Post

register = template.Library()
@register.inclusion_tag('blog/latest_post.html')
def latest_post():
    context = {
        'l_posts': Post.objects.all()[0:5],
    }

    return context