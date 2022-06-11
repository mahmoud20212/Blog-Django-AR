from django.shortcuts import redirect, render

from blog.models import Post
from .forms import UserCreationForm, LoginForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def register(request):
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            # username = form.cleaned_data['username']
            messages.success(request, f'تهانينا {new_user} لقد تمت عملية التسجيل بنجاح.')
            return redirect('login')
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
            return redirect('profile')
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

@login_required(login_url='login')
def profile(request):
    posts = Post.objects.filter(author=request.user)
    posts_list = Post.objects.filter(author=request.user)
    paginator = Paginator(posts_list, 10)
    page = request.GET.get('page')
    try:
        posts_list = paginator.page(page)
    except PageNotAnInteger:
        posts_list = paginator.page(1)
    except EmptyPage:
        posts_list = paginator.page(paginator.num_page)
    context = {
        'title': 'الملف الشخصي',
        'posts': posts,
        'page': page,
        'posts_list': posts_list,
    }
    return render(request, 'user/profile.html', context)

@login_required(login_url='login')
def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid and profile_form.is_valid:
            user_form.save()
            profile_form.save()
            messages.success(request, 'تم تحديث الملف الشخصي.')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'title': 'تعديل الملف الشخصي',
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'user/profile_update.html', context)


