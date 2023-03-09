# from django.contrib import messages
# from django.db.models import Q
# from django.views.generic import (
#     DetailView,
#     ListView,
# )
# from phim.models.movie_model import Movie
# from phim.models.category_model import Category

# class MovieListView(ListView):
#     context_object_name = "movies"
#     paginate_by = 12
#     queryset = Movie.objects.filter(status=Movie.created.FULLHD, deleted=False)
#     template_name = "phim/home.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['categories'] = Category.objects.filter(approved=True)
#         return context