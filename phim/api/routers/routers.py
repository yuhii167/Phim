from django.urls import path

from phim.api.views.category_views import CategoryList

urlpatterns = [
    path('categories/', CategoryList.as_view()),
]