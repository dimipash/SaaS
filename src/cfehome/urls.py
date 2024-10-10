from django.contrib import admin
from django.urls import path, include
from auth import views as auth_views
from .views import home_view, about_view, pw_protected_view

urlpatterns = [
    path("", home_view, name="home"),  # index page -> root page
    path("about/", about_view),
    path("login/", auth_views.login_view),
    path("register/", auth_views.register_view),
    path("hello-world/", home_view),
    path("hello-world.html", home_view),
    path("accounts/", include("allauth.urls")),
    path("protected/", pw_protected_view),
    path("admin/", admin.site.urls),
]
