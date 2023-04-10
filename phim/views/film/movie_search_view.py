from django.shortcuts import render
from django.views.generic import View
from phim.models.movie_model import MovieSearch
from django.core.paginator import Paginator

class SearchResultView(View):
    template_name = 'phim/search_results.html'
    paginate_by = 100

    def get(self, request, *args, **kwargs):
        query_params = request.GET.copy()
        filters = MovieSearch.get_filters(request)
        movies = MovieSearch.search_movies(filters)

        paginator = Paginator(movies, self.paginate_by)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'movies': page_obj,
            'categories': MovieSearch.get_categories(),
            'tags': MovieSearch.get_tags(),
            'years': MovieSearch.get_years(),
            'countries': MovieSearch.get_countries(),
            'filters': filters,
            'query_params': query_params,
        }

        return render(request, self.template_name, context)
