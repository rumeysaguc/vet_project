from django.contrib import admin
from .views import animal_detail
from django.urls import path

app_name="animal/"

urlpatterns = [
    path('animal-detail/<int:id>', animal_detail, name='animal-detail'),


]