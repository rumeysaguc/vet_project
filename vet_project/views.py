from django.shortcuts import render

from animal.models import Animal


def main(request):
    animals = Animal.objects.all()

    return render(request,"index.html",{'animals':animals})
