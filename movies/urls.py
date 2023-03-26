from django.urls import path

from . import views


urlpatterns = [
    path("", views.MoviesView.as_view()),
    path("<slug:slug>/", views.MovieDetailView.as_view(), name="moviesingle"),
    path("review/<int:pk>/", views.AddRewiew.as_view(), name="add_review"),
    path("actor/<str:slug>/", views.ActorView.as_view(), name="actor_detail"),
]