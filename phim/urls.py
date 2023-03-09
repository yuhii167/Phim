from django.urls import path

from phim.views.account.register_view import UserRegisterView


from phim.views.account.logout_view import UserLogoutView
from phim.views.account.login_view import UserLoginView
from phim.views.account.user_view import UserView
#from phim.views.film.movie_view import MovieListView

app_name = "phim"

urlpatterns = [ 
    # account/login/
    path(
        route='account/login/',
        view=UserLoginView.as_view(),
        name='login'
    ),

    # account/login/
    path(
        route='account/register/',
        view=UserRegisterView.as_view(),
        name='register'
    ),

    # account/logout/
    path(
        route='account/logout/',
        view=UserLogoutView.as_view(),
        name='logout'
    ),
    #category-phim/<str:slug>/
    # path(
    #     route='category/<str:slug>/phim',
    #     view=CategoryMovieListView.as_view(),
    #     name='category_phim'
    # ),

    #home
    path(
        route='',
        view=UserView.as_view(),
        name='home'
    ),

    
]