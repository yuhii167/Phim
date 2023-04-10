from phim.models.movie_model import MovieSearch

def categories(request):
    categories = MovieSearch.get_categories()
    return {'categories': categories}

def tags(request):
    tags = MovieSearch.get_tags()
    return {'tags': tags}

def years(request):
    years = MovieSearch.get_years()
    return {'years': years}

def countries(request):
    countries = MovieSearch.get_countries()
    return {'countries': countries}