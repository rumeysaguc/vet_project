from django.contrib.auth.models import User
from django.shortcuts import render

from animal.forms import AnimalForm
from animal.models import Animal, Contact

def add_animal_page(request):
    form = AnimalForm()
    return render(request,"add_animal.html",{'form':form})

def delete(request,id):
    Animal.objects.filter(id=id).delete()
    animals = Animal.objects.all()
    return render(request, "animals_list.html", {'animals':animals})

def add_animal(request):
    form = AnimalForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
    else:
        form = AnimalForm()

    return render(request,"success.html",{'form':form})

def animal_detail(request, id):
    user = User.objects.get(id=id)
    contact = Contact.objects.get(user_id=id)
    animals = Animal.objects.filter(owner_id=id).all()
    return render(request,"animal_detail.html",{'animals':animals,'user':user,'contact':contact})