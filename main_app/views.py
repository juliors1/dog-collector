from django.shortcuts import render

class Dog:
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

dogs = [
  Dog('Lolo', 'tabby', 'foul little demon', 3),
  Dog('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
  Dog('Raven', 'black tripod', '3 legged dog', 4)
]

# Define the home view
def home(request):
    return HttpResponse("<h1>Hello World</h1>")


def about(request):
    return render(request, "about.html")


def dogs_index(request):
    return render(request, "dogs/index.html", {"dogs": dogs})
