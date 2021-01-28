from django.shortcuts import render
from .models import Dog

# Create your views here

def home(request):
    return HttpResponse("<h1>Hello World</h1>")


def about(request):
    return render(request, "about.html")


def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, "dogs/index.html", {"dogs": dogs})
