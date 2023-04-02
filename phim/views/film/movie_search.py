from django.shortcuts import render
from django.views.generic import TemplateView
from phim.models.movie_model import MovieSearch

class HomeViewSearch(TemplateView):
    template_name = 'phim_base.html'

    def get(self, request, *args, **kwargs):
        categories = MovieSearch.get_categories()
        tags = MovieSearch.get_tags()
        release_years = MovieSearch.get_release_years()

        filters = MovieSearch.get_filters(request)
        movies = MovieSearch.search_movies(filters)

        context = {
            'categories': categories,
            'tags': tags,
            'release_years': release_years,
            'movies': movies,
        }

        return self.render_to_response(context)
