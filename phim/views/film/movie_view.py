from django.db.models import Q
from django.views.generic import (
    DetailView,
    ListView,
)
from phim.models.movie_model import Movie
from phim.models.category_model import Category
from phim.models.ads_model import Ads
from phim.models.actor import Actor

class MovieListView(ListView):
    context_object_name = "movies"
    paginate_by = 12
    template_name = 'phim/home.html'

    def get_queryset(self):
        return Movie.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['adss'] = Ads.objects.all()
        return context
    
class MovieListView1(ListView):
    context_object_name = "movies"
    paginate_by = 12
    queryset = Movie.objects.all()
    template_name = 'phim/phim.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies'] = Movie.objects.all()
        return context
    
class MovieDetailView(DetailView):
    model = Movie
    template_name = 'phim/phimdetail.html'

    def get_context_data(self, **kwargs):
        session_key = f"viewed_movie {self.object.slug}"
        self.object.views += 1
        self.object.save()
        self.request.session[session_key] = True

        kwargs['movie'] = self.get_object

        return super().get_context_data(**kwargs)
    
