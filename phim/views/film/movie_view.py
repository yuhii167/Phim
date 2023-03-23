from django.db.models import Q
from django.views.generic import (
    DetailView,
    ListView,
)
from django.shortcuts import render
from phim.models.movie_model import Movie
from phim.models.category_model import Category
from phim.models.ads_model import Ads
from phim.models.actor import Actor

#View phim trang chủ
class MovieListView(ListView):
    model = Movie
    template_name = 'phim/home.html'
    context_object_name = 'movies'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
       
        context['le_movies'] = Movie.objects.filter(category='2')
        context['bo_movies'] = Movie.objects.filter(category='3')
        return context


#View Phim trang Phim
class MovieListView1(ListView):
    context_object_name = "movies"
    queryset = Movie.objects.all()
    template_name = 'phim/phim.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

#Chi tiết
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
    
#Phim bộ
class PhimBoListView(ListView):
    context_object_name = "movies"
    queryset = Movie.objects.filter(category='3')
    template_name = 'phim/phim_bo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
#Phim lẻ
class PhimLeListView(ListView):
    context_object_name = "movies"
    queryset = Movie.objects.filter(category='2')
    template_name = 'phim/phim_le.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    
