from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Genre(models.Model):

    name = models.CharField( max_length = 100 )
    description = models.TextField()

    def __str__(self):
        return self.name


class Movie(models.Model):

    genre = models.ManyToManyField(Genre)
    name = models.CharField(max_length = 100)
    story_line = models.TextField()
    release_date = models.DateField()
    duration = models.CharField(max_length=10)
    poster = models.ImageField(upload_to="images/")


    def __str__(self):
        return self.name



class Review(models.Model):

    Rating = [(1 , "1"),
              (2 , "2"),
              (3 , "3"),
              (4 , "4"),
              (5 , "5")]

    user = models.OneToOneField(User , on_delete = models.CASCADE)
    movie = models.ForeignKey(Movie , on_delete = models.CASCADE)
    comment = models.TextField( null= True , blank = True)
    rating = models.CharField(max_length= 1 , choices= Rating)
    created_at = models.DateTimeField(auto_now_add = True , blank = True)



class Watchlist(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    movie = models.ManyToManyField(Movie)