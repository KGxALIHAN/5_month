from django.urls import path
from .views import (
    DirectorListAPIView,
    DirectorCreateAPIView,
    DirectorDetailAPIView,
    MovieListAPIView,
    MovieCreateAPIView,
    MovieDetailAPIView,
    ReviewListAPIView,
    ReviewCreateAPIView,
    ReviewDetailAPIView,
)

urlpatterns = [
    path('directors/', DirectorListAPIView.as_view(), name='director-list'),
    path('directors/create/', DirectorCreateAPIView.as_view(), name='director-create'),
    path('directors/<int:pk>/', DirectorDetailAPIView.as_view(), name='director-detail'),
    path('movies/', MovieListAPIView.as_view(), name='movie-list'),
    path('movies/create/', MovieCreateAPIView.as_view(), name='movie-create'),
    path('movies/<int:pk>/', MovieDetailAPIView.as_view(), name='movie-detail'),
    path('reviews/', ReviewListAPIView.as_view(), name='review-list'),
    path('reviews/create/', ReviewCreateAPIView.as_view(), name='review-create'),
    path('reviews/<int:pk>/', ReviewDetailAPIView.as_view(), name='review-detail'),
]
