from django.urls import path, include
from phim.views.account.register_view import UserRegisterView


from phim.views.account.logout_view import UserLogoutView
from phim.views.account.login_view import UserLoginView
from phim.views.film.actor_view import ActorListView
from phim.views.film.movie_view import MovieListView
from phim.views.film.movie_view import MovieListView1
from phim.views.film.movie_view import PhimBoListView
from phim.views.film.movie_view import PhimLeListView
from phim.views.film.movie_view import MovieDetailView
from phim.views.account.user_view import ProfileUserView
from phim.views.film.get_api_model_movie import update_movie
from phim.views.film.get_data_movie import update_movie1

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
    path("update_movie/", update_movie, name="update_movie"),
    path("update_movie1/", update_movie1, name="update_movie"),
    #API google
    # path('accounts/', include('allauth.urls')),

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
        route='movie/series',
        view=PhimBoListView.as_view(),
        name='series'

    ), 

    path(
        route='movie/film',
        view=PhimLeListView.as_view(),
        name='film'

    ), 

    path(
        route='movie/<str:slug>/',
        view=MovieDetailView.as_view(),
        name='phimdetail'

    ),

    #user
    path(
        route='user/profile',
        view=ProfileUserView.as_view(),
        name='user_profile'

    ),


    
]
