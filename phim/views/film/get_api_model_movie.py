import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from phim.models.movie_model import Movie
from django.contrib import messages
from phim.models.category_model import Category


def update_movie(request):
    if request.method == 'POST':
        imdb_url = request.POST.get('imdb_url')

        response = requests.get(imdb_url)

        soup = BeautifulSoup(response.content, 'html.parser')

        title = soup.select_one('h1').text

        movie = Movie()
        movie.title = title
        print(movie.title)

            # Lấy thể loại phim
        categories = []
        category_tags = soup.find_all('a', {' .content_detail content_min fl'})
        for tag in category_tags:
            categories.append(tag.text.strip())

            # Tạo thể loại mới nếu chưa tồn tại
        for category_name in categories:
            category, _ = Category.objects.get_or_create(name=category_name)
            movie.category.add(category)

        movie.save()

        messages.success(request, 'Cập nhật phim thành công.')

    return render(request, 'phim/update_movie.html')

