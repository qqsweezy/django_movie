from django import template
from movies.models import Category
from movies.models import Movie


register = template.Library()


@register.simple_tag()
def get_categories():
    """Output all categorys"""
    return Category.objects.all()


@register.inclusion_tag('movies/tags/last_movie.html')
def get_last_movies(count):
    movies = Movie.objects.order_by("id")[:count]
    return {"last_movies": movies}
