from django.shortcuts import render


# Define the home view
def home(request):
    return HttpResponse("<h1>Hello World</h1>")


def about(request):
    return render(request, "about.html")


def dogs_index(request):
    return render(request, "dogs/index.html", {"dogs": dogs})
