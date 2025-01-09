from django.urls import path
from .views import (
    DirectorListAPIView,
    DirectorDetailAPIView,
    MovieListAPIView,
    MovieDetailAPIView,
    ReviewListAPIView,
    ReviewDetailAPIView,
    MoviesWithReviewsAPIView,
)

urlpatterns = [
    path('directors/', DirectorListAPIView.as_view(), name='director-list'),
    path('directors/<int:pk>/', DirectorDetailAPIView.as_view(), name='director-detail'),
    path('movies/', MovieListAPIView.as_view(), name='movie-list'),
    path('movies/<int:pk>/', MovieDetailAPIView.as_view(), name='movie-detail'),
    path('movies/reviews/', MoviesWithReviewsAPIView.as_view(), name='movies-with-reviews'),
    path('reviews/', ReviewListAPIView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetailAPIView.as_view(), name='review-detail'),
]
