from django.urls import path
from django.contrib.auth.views import LoginView , LogoutView
from .views import Register , MovieListView , MovieDetailView , CreateReview

urlpatterns = [
    path("register/", Register.as_view() , name= "register" ),
    path("login/", LoginView.as_view(template_name="MovieApp/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("",MovieListView.as_view(),name="list-movies"),
    path("movies/<int:pk>/", MovieDetailView.as_view(), name="movie-detail"),
    path("movies/<int:pk>/review/", CreateReview.as_view(), name="create-review")

]
