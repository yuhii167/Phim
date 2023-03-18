import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from phim.models.movie_model import Movie
from django.contrib import messages
from phim.models.category_model import Category
import cloudinary
import cloudinary.uploader

def update_movie(request):
    if request.method == 'POST':
        imdb_url = request.POST.get('imdb_url')

        response = requests.get(imdb_url)

        soup = BeautifulSoup(response.content, 'html.parser')

        title = soup.select_one('h1').text
        title_el = soup.select_one('h2').text
        description = soup.select_one(' .text > .text-content').text
        rating = soup.select_one('.featured-attr:contains("IMDB") .text').text
        contry = soup.select_one('.featured-attr:contains("Quốc gia") .text').text
        year = soup.select_one('.featured-attr:contains("Năm phát hành") .text').text
        time = soup.select_one('.featured-attr:contains("Thời lượng") .text').text
        images = soup.select_one('.col-md-3 > .media.media-cover')['data-src']
        image_url = cloudinary.uploader.upload(images)
        print(image_url)
        

        movie = Movie()
        movie.title = title
        movie.description = description
        movie.title_el = title_el
        movie.rating = rating
        movie.contry = contry
        movie.year = year
        movie.time = time
        movie.flyer = image_url['secure_url']
     
        
        print(movie.title)
        print(movie.rating)

            # Lấy thể loại phim
        

        movie.save()

        messages.success(request, 'Cập nhật phim thành công.')

    return render(request, 'phim/update_movie.html')

