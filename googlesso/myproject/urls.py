from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('myapp.urls')),

    path("google_sso/", include("django_google_sso.urls", namespace="django_google_sso")),
]
