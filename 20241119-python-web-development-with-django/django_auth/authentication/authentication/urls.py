"""
URL configuration for authentication project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from account import views as account_views
from app import views as app_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", account_views.landing_view, name="home"),
    path("home/", account_views.home_view, name="home"),
    path("register/", account_views.register_view, name="register"),
    path("login/", account_views.login_view, name="login"),
    path("logout/", account_views.logout_view, name="logout"),
    path("base/", app_views.base_view, name="base"),
    path("base/apple/", app_views.child_apple_view, name="child-apple"),
    path("orange/", app_views.child_orange_view, name="child-orange"),
]
