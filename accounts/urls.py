from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view),
    path("login/", login_view),
    path("logout/", logout_view)
]