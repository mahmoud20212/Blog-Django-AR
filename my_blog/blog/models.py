from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class Setting(models.Model):
    site_title = models.CharField(_('site title'), max_length=255)
    tagline = models.CharField(
        _('tagline'),
        max_length=255,
        help_text=_('In a few words, explain what this site is about. Example: “Just another WordPress site.”'),
    )
    keywords = models.CharField(_('keywords'), max_length=255, null=True, blank=True)
    bio = models.CharField(_('bio'), max_length=255, null=True, blank=True)
    site_icon = models.ImageField(
        _('site icon'),
        upload_to='logo_pics',
        help_text=_('The Site Icon is what you see in browser tabs, bookmark bars, and within the WordPress mobile apps. It should be square and at least 512 by 512 pixels.'),
    )
    logo = models.ImageField(_('logo'), upload_to='logo_pics')

    def __str__(self):
        return "General Settings"

    class Meta:
        verbose_name = _("Setting")


class About(models.Model):
    description = models.TextField(_('description'))

    def __str__(self):
        return "About Information"

    class Meta:
        verbose_name = _("About")

class Post(models.Model):
    title = models.CharField(_('title'), max_length=100)
    slug = models.SlugField(
        max_length=250,
        null=True,
        blank=True,
        unique_for_date='post_date',
    )
    content = models.TextField(_('content'))
    post_date = models.DateTimeField(_('post date'), default=timezone.now)
    post_update = models.DateTimeField(_('post update'), auto_now=True)
    author = models.ForeignKey(User, verbose_name=_('author'), on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)
    
    def get_absolute_url(self):
        # return f'/detail/{self.pk}'
        return reverse('detail', args=[
            self.post_date.year,
            self.post_date.month,
            self.post_date.day,
            self.slug
        ])
    
    class Meta:
        ordering = ['-post_date']
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

class Comment(models.Model):
    name = models.CharField(_('name'), max_length=50)
    email = models.EmailField(_('email'))
    body = models.TextField(_('body'))
    comment_date = models.DateTimeField(_('comment date'), auto_now_add=True)
    active = models.BooleanField(_('active'), default=False)
    post = models.ForeignKey(Post, verbose_name=_('post'), on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return _('comment %(name)s on %(post)s.') % {'name': self.name, 'post': self.post}

    class Meta:
        ordering = ['-comment_date']
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")