from django.urls import path
from app.api import views

urlpatterns = [
    path('Stream_platform_lists/', views.StreamPlatformListsAV.as_view(),name='stream'),
    path('Stream_platform_lists/<int:pk>/', views.StreamPlatFormDetailsAV.as_view(),name='stream_details'),
    path('watch_lists/', views.WatchListListAV.as_view(),name='list'),
    path('watch_list_details/<int:pk>/', views.WatchListDetailsAV.as_view(),name='details'),

    # path('list/', views.MovieListAV.as_view(), name='list'),
    # path('list/', views.movie_list, name='movie_list'),
    # path('list/<int:pk>/', views.movie_details, name='movie'),

    # path('list/', views.MovieListAV.as_view(), name='list'),
    # path('<int:pk>/', views.MovieDetailsAV.as_view(), name='details'),
    # path('list/', views.MovieListAV.as_view(), name='list'),
    # path('list/', views.movie_list, name='movie_list'),
    # path('list/<int:pk>/', views.movie_details, name='movie'),
]
