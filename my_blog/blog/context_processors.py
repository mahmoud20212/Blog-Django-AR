from django.contrib.auth.models import User
from .models import Setting

def setting(request):
    setting = Setting.objects.first()
    return {'setting': setting}

def author(request):
    return {'author': User.objects.first()}