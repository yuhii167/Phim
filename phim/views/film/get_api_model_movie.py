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
        title_el = soup.select_one('h2').text
        rating = soup.select_one('.featured-attr:contains("IMDB") .text').text
        contry = soup.select_one('.featured-attr:contains("Quốc gia") .text').text
        year = soup.select_one('.featured-attr:contains("Năm phát hành") .text').text
        time = soup.select_one('.featured-attr:contains("Thời lượng") .text').text
        flyer = soup.select_one('div', class_='media media-cover mb-2')

        movie = Movie()
        movie.title = title
        movie.title_el = title_el
        movie.rating = rating
        movie.contry = contry
        movie.year = year
        movie.time = time
        movie.flyer = flyer
        
        print(movie.title)
        print(movie.rating)

            # Lấy thể loại phim
        

        movie.save()

        messages.success(request, 'Cập nhật phim thành công.')

    return render(request, 'phim/update_movie.html')

