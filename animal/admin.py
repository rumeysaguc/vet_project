from django.contrib import admin
from animal.models import Animal,AnimalType

class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'age', 'genus')

class AnimalTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(AnimalType,AnimalTypeAdmin)
admin.site.register(Animal,AnimalAdmin)