from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('detail/<int:pk>', views.post_detail, name='detail'),
]