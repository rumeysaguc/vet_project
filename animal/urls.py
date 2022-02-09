from django.contrib import admin
from .views import *
from django.urls import path

app_name = "animal/"

urlpatterns = [
    path('animal-detail/<int:id>', animal_detail, name='animal-detail'),
    path('add-animal', add_animal, name='add-animal'),
    path('delete-animal/<int:id>', delete, name='delete-animal'),
    path('add-animal-page', add_animal_page, name='add-animal-page'),

]