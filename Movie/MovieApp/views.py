from django.shortcuts import render 
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.views.generic import CreateView , ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Movie


class Register(CreateView):
    form_class = RegisterForm
    template_name = "MovieApp/register.html"
    success_url = reverse_lazy("login")


class MovieListView(ListView):
    model = Movie
    template_name = "MovieApp/movie_list.html"
    context_object_name = "movies"
    paginate_by = 16

