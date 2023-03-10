from django.views.generic import (
    DetailView,
    ListView,
)

from phim.models.actor import Actor

class ActorListView(ListView):
    context_object_name = "actores"
    paginate_by = 12
    queryset = Actor.objects.all()
    template_name = 'phim/actor.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['actores'] = Actor.objects.all()
        return context