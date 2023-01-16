from django.contrib import admin
from django.urls import path, include
from register import views as v
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", v.register, name="register"),
    path('', include("django.contrib.auth.urls")),
    path("<int:id>", views.index, name="index"),
    path("", views.home, name="home.html"),
    path("view/", views.view, name="view"),


]