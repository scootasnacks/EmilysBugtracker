from django.contrib import admin
from django.urls import path, include
from register import views as v
from . import views
from django.urls import path
from .views import user_page

urlpatterns = [
    # other URL patterns here...
    path('user_page/', user_page, name='user_page'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", v.register, name="register"),
    path('', include("django.contrib.auth.urls")),
    path("<int:id>", views.index, name="index"),
    path("", views.home, name="home.html"),
    path("view/", views.view, name="view"),

]