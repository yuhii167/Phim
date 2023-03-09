from django.shortcuts import redirect, render
from django.views import View

class UserView(View):
    def get(self,request,*args, **kwargs):
        return render(request,'phim/home.html')