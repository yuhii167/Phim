from django.urls import path

from phim.views.account.register_view import UserRegisterView


from phim.views.account.logout_view import UserLogoutView
from phim.views.account.login_view import UserLoginView
from phim.views.film.actor_view import ActorListView
from phim.views.film.movie_view import MovieListView
from phim.views.film.movie_view import MovieListView1
from phim.views.film.movie_view import MovieDetailView

app_name = "phim"

urlpatterns = [ 
    # account/login/
    path(
        route='login/',
        view=UserLoginView.as_view(),
        name='login'
    ),

    # account/login/
    path(
        route='register/',
        view=UserRegisterView.as_view(),
        name='register'
    ),

    # account/logout/
    path(
        route='logout/',
        view=UserLogoutView.as_view(),
        name='logout'
    ),
    #category-phim/<str:slug>/
    path(
        route='category/<str:slug>/phim',
        view=MovieListView.as_view(),
        name='category_phim'
    ),

    #home
    path(
        route='',
        view=MovieListView.as_view(),
        name='home'
    ),

    #actor
    path(
        route='actor/',
        view=ActorListView.as_view(),
        name='actor'
    ),

    #phim
    path(
        route='movie/',
        view=MovieListView1.as_view(),
        name='movie'
    ),

     path(
        route='movie/<str:slug>/',
        view=MovieDetailView.as_view(),
        name='phimdetail'

    ),

    
]