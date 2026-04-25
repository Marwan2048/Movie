from django.contrib import admin
from .models import Genre , Movie , Watchlist , Review
# Register your models here.


admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Watchlist)
admin.site.register(Review)
