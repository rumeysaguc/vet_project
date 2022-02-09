"""vet_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include, re_path
from django.utils.translation import gettext_lazy as _

from vet_project.views import main, login_user, signup, signup_page
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('super/admin/', admin.site.urls),
    path('', main, name='mainPage'),
    path('login', login_user, name='login'),
    path('signup-page', signup_page, name='signup-page'),
    path('signup', signup, name='signup'),
    path(_('account/'), include("allauth.urls")),
    path(_('animal/'), include("animal.urls")),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),


]
