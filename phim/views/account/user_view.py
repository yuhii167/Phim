from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import User

class ProfileUserView(LoginRequiredMixin, View):

    template_name = "phim/user_profile.html"
    context_object = {}

    def get(self, request):
        user = User.objects.get(username = request.user)

        self.context_object['user_profile'] = user 
        return render (request, self.template_name, self.context_object)
