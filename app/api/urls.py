from django.urls import path
from app.api import views

urlpatterns = [
    path('list/', views.MovieListAV.as_view(), name='list'),
    path('<int:pk>/', views.MovieDetailsAV.as_view(), name='details'),
    # path('list/', views.MovieListAV.as_view(), name='list'),
    # path('list/', views.movie_list, name='movie_list'),
    # path('list/<int:pk>/', views.movie_details, name='movie'),
]
