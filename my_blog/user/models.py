from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _
from PIL import Image

class Profile(models.Model):
    image = models.ImageField(_('image'), default='avatar.jpg', upload_to='profile_pics')
    user = models.OneToOneField(User, verbose_name=_('user'), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.width > 300 or img.height > 300:
            img.thumbnail((300, 300))
            img.save(self.image.path)

def create_profile(sender, **kwarg):
    if kwarg['created']:
        Profile.objects.create(user=kwarg['instance'])

post_save.connect(create_profile, sender=User)