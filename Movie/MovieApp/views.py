from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm , CreateReviewForm
from django.views.generic import CreateView , ListView , DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Movie  , Genre , Review
from django.shortcuts import redirect


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
        context["form"] = CreateReviewForm()
        return context
    

class CreateReview(LoginRequiredMixin , CreateView):
    template_name = "MovieApp/create_review.html"
    form_class = CreateReviewForm
    model = Review
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.movie = Movie.objects.get(id = self.kwargs["pk"])
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("movie-detail", kwargs = {"pk":self.object.movie.id})


        
    

    
