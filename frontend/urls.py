from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('create/', views.post_create, name='post_create'),
    path('posts/<int:pk>/edit/', views.edit_post, name='edit_post'),
    path('posts/<int:pk>/comment/', views.add_comment, name='add_comment'),
    path('posts/<int:pk>/like/', views.add_like, name='add_like'),
    path('posts/<int:pk>/unlike/', views.remove_like, name='remove_like'),
    path('posts/<int:pk>/delete/', views.delete_post, name='delete_post'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
]