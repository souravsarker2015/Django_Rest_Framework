from django.http import JsonResponse
from django.shortcuts import render
from app.models import *


def movie_list(request):
    movies = Movie.objects.all()

    data = {
        'movies': list(movies.values())
    }
    return JsonResponse(data)


def movie_details(request, pk):
    movie = Movie.objects.get(id=pk)
    print(movie.name)
    print(movie.description)
    data = {
        'name': movie.name,
        'description': movie.description,
        'active': movie.active,
    }
    return JsonResponse(data)
