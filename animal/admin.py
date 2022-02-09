from django.contrib import admin
from animal.models import Animal, AnimalType, Contact


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'age', 'genus')

class AnimalTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('user','phone','address')

admin.site.register(AnimalType,AnimalTypeAdmin)
admin.site.register(Animal,AnimalAdmin)
admin.site.register(Contact,ContactAdmin)