from django.contrib import messages
from django.db.models import Q
from django.views.generic import (
    DetailView,
    ListView,
)
from phim.models.movie_model import Movie
from phim.models.category_model import Category

class MovieListView(ListView):
    context_object_name = "movies"
    paginate_by = 12
    context_object_name = 'momies'
    template_name = 'phim/home.html'

    def get_queryset(self):
        return Movie.objects.all().order_by('-date_created')