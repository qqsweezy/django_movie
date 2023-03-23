from django.shortcuts import render, redirect
from .models import Actor, Category, Genre, Movie, RaitingStar, Reviews, Raiting
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .forms import ReviewForm


class MoviesView(ListView):
    """List movies"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    #template_name = "movies/movies.html"
    #return render(request, "movies/movies.html", {"movie_list": movies})


class MovieDetailView(DetailView):
    """Description movie"""
    model = Movie
    slug_field = "url"


class AddRewiew(View):
    """Rewiews"""
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())
