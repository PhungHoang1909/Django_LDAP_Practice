from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Trang chủ
    path('profile/', views.profile, name='profile'),  # Trang hồ sơ người dùng
    path('login/', views.custom_login, name='login'),
]
