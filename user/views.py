from django.shortcuts import redirect, render

from blog.models import Post
from .forms import UserCreationForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def register(request):
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'تهانينا {username} لقد تمت عملية التسجيل بنجاح.')
            return redirect('index')
    else:
        form = UserCreationForm()
    context = {
        'title': 'التسجيل',
        'form': form,
    }
    return render(request, 'user/register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = LoginForm()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.warning(request, 'هناك خطأ في إسم المستخدم أو كلمة المرور.')
    else:
        form = LoginForm()

    context = {
        'title': 'تسجيل الدخول',
        'form': form,
    }
    return render(request, 'user/login.html', context)

def logout_user(request):
    logout(request)
    context = {
        'title': 'تسجيل الخروج',
    }
    return render(request, 'user/logout.html', context)

def profile(requset):
    posts = Post.objects.filter(author=requset.user)
    context = {
        'title': 'الملف الشخصي',
        'posts': posts,
    }
    return render(requset, 'user/profile.html', context)
