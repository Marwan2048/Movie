from django.db import models
from django.contrib.auth.models import User 
from django.core.validators import MinValueValidator
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
    duration = models.PositiveIntegerField(validators = [MinValueValidator(1)])
    poster = models.ImageField(upload_to="images/")

    @property
    def duration_format(self):
        duration = int(self.duration)
        hours = self.duration // 60
        minutes = self.duration % 60

        return f"{hours}h:{minutes:02d}m"

    def __str__(self):
        return self.name



class Review(models.Model):

    Rating = [(1 , "1"),
              (2 , "2"),
              (3 , "3"),
              (4 , "4"),
              (5 , "5")]

    user = models.ForeignKey(User , on_delete = models.CASCADE)
    movie = models.ForeignKey(Movie , on_delete = models.CASCADE)
    comment = models.TextField( null= True , blank = True)
    rating = models.IntegerField(choices= Rating)
    created_at = models.DateTimeField(auto_now_add = True , blank = True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user} : {self.rating}"



class Watchlist(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    movie = models.ManyToManyField(Movie)