from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='detail'),
    path('about/', views.about, name='about'),
    path('new_post/', views.PostCreateView.as_view(), name='new_post'),
    path('detail/<slug:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('detail/<slug:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
]