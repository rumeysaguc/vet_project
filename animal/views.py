from django.shortcuts import render

from animal.models import Animal

def animal_detail(request, id):
    animal = Animal.objects.get(id=id)
    return render(request,"animal_detail.html",{'animal':animal})