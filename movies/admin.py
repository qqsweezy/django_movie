from django.contrib import admin
from .models import MovieShots, Actor, Category, Genre, Movie, RaitingStar, Reviews, Raiting

admin.site.register(Category)
admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Genre)

admin.site.register(RaitingStar)
admin.site.register(Raiting)
admin.site.register(Reviews)
admin.site.register(MovieShots)
