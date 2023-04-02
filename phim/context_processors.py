from phim.models.movie_model import MovieSearch

def categories(request):
    categories = MovieSearch.get_categories()
    return {'categories': categories}

def tags(request):
    tags = MovieSearch.get_tags()
    return {'tags': tags}

def release_years(request):
    release_years = MovieSearch.get_release_years()
    return {'release_years': release_years}

def countries(request):
    countries = MovieSearch.get_countries()
    return {'countries': countries}