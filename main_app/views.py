from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Dog, Toy
from .forms import FeedingForm

# Create your views here
class DogCreate(CreateView):
    model = Dog
    fields = "__all__"


class DogUpdate(UpdateView):
    model = Dog
    fields = ["breed", "description", "age"]


class DogDelete(DeleteView):
    model = Dog
    success_url = "/dogs/"


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, "dogs/index.html", {"dogs": dogs})


def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    # instantiate FeedingForm to be rendered in the template
    feeding_form = FeedingForm()
    return render(
        request, "dogs/detail.html", {"dog": dog, "feeding_form": feeding_form}
    )


def add_feeding(request, dog_id):
    # create a ModelForm instance using the data in request.POST
    form = FeedingForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the dog_id assigned
        new_feeding = form.save(commit=False)
        new_feeding.dog_id = dog_id
        new_feeding.save()
    return redirect("detail", dog_id=dog_id)

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'

