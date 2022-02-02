from django.urls import path
from app.api import views

urlpatterns = [
    path('stream/', views.StreamPlatformListsAV.as_view(), name='stream'),
    path('stream/<int:pk>/', views.StreamPlatFormDetailsAV.as_view(), name='stream_details'),
    path('lists/', views.WatchListListAV.as_view(), name='list'),
    path('list_details/<int:pk>/', views.WatchListDetailsAV.as_view(), name='details'),
    path('review/', views.ReviewList.as_view(), name='review'),
    path('review/<int:pk>/', views.ReviewDetail.as_view(), name='review_details'),

]

# path('list/', views.MovieListAV.as_view(), name='list'),
# path('list/', views.movie_list, name='movie_list'),
# path('list/<int:pk>/', views.movie_details, name='movie'),

# path('list/', views.MovieListAV.as_view(), name='list'),
# path('<int:pk>/', views.MovieDetailsAV.as_view(), name='details'),
# path('list/', views.MovieListAV.as_view(), name='list'),
# path('list/', views.movie_list, name='movie_list'),
# path('list/<int:pk>/', views.movie_details, name='movie'),
