from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import render,redirect
from django.views.generic import View


class UserLogoutView(View):

    template_name = 'account/home.html'

    def get(self, request):
        logout(request)
        messages.success(request, "Bạn đã đăng xuất!")
        return render(request,self.template_name)