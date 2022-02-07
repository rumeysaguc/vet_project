from django.contrib import admin
from .views import animal_detail
from django.urls import path

urlpatterns = [
    path('animal-detail', animal_detail, name='animal-detail'),


]