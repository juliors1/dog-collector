from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Dog, Toy
from .forms import FeedingForm

# Create your views here
class DogCreate(CreateView):
    model = Dog
    fields =  ['name', 'breed', 'description', 'age']
    # This inherited method is called when a
    # valid cat form is being submitted
    def form_valid(self, form):
    # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
        return super().form_valid(form)

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
    dogs = Dog.objects.filter(user=request.user)
    return render(request, "dogs/index.html", {"dogs": dogs})


def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    # Get the toys the dog doesn't have
    toys_dog_doesnt_have = Toy.objects.exclude(id__in=dog.toys.all().values_list("id"))
    # instantiate FeedingForm to be rendered in the template
    feeding_form = FeedingForm()
    return render(
        request,
        "dogs/detail.html",
        {
            "dog": dog,
            "feeding_form": feeding_form,
            # Add the toys to be displayed
            "toys": toys_dog_doesnt_have,
        },
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


def assoc_toy(request, dog_id, toy_id):
    # Note that you can pass a toy's id instead of the whole object
    Dog.objects.get(id=dog_id).toys.add(toy_id)
    return redirect("detail", dog_id=dog_id)


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class ToyList(ListView):
    model = Toy


class ToyDetail(DetailView):
    model = Toy


class ToyCreate(CreateView):
    model = Toy
    fields = "__all__"


class ToyUpdate(UpdateView):
    model = Toy
    fields = ["name", "color"]


class ToyDelete(DeleteView):
    model = Toy
    success_url = "/toys/"
