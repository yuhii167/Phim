from django.shortcuts import render
from django.views.generic import TemplateView
from phim.models.movie_model import MovieSearch

class HomeViewSearch(TemplateView):
    template_name = 'phim_base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = MovieSearch.get_categories()
        context['tags'] = MovieSearch.get_tags()
        context['years'] = MovieSearch.get_years()
        context['countries'] = MovieSearch.get_countries()

        filters = MovieSearch.get_filters(self.request)
        movies = MovieSearch.search_movies(filters)
        context['movies'] = movies

        return context

    def post(self, request, *args, **kwargs):
        filters = MovieSearch.get_filters(request)
        movies = MovieSearch.search_movies(filters)

        context = {
            'categories': MovieSearch.get_categories(),
            'tags': MovieSearch.get_tags(),
            'years': MovieSearch.get_years(),
            'countries': MovieSearch.get_countries(),
            'movies': movies,
            'filters': filters,
        }

        return render(request, self.template_name, context)
