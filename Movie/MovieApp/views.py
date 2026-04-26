from django.shortcuts import render 
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm , CreateReviewForm
from django.views.generic import CreateView , ListView , DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Movie  , Genre , Review


class Register(CreateView):
    form_class = RegisterForm
    template_name = "MovieApp/register.html"
    success_url = reverse_lazy("login")


class MovieListView(ListView):
    model = Movie
    template_name = "MovieApp/movie_list.html"
    context_object_name = "movies"
    paginate_by = 16


class MovieDetailView(DetailView):

    model = Movie
    template_name = "MovieApp/movie_detail.html"
    context_object_name = "movie"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movie_id = self.kwargs["pk"]
        context["reviews"] = Review.objects.filter(movie__id = movie_id)
        return context
        

class ReviewCreateView(LoginRequiredMixin ,CreateView):
    model = Review
    form_class = CreateReviewForm
    template_name = "MovieApp/review_form.html"
    context_object_name = "review"







