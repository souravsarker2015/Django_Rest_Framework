from django.urls import path
from app import views

urlpatterns = [
    path('list/', views.movie_list, name='movie'),
    path('details/<int:pk>/', views.movie_details, name='movie'),
]
