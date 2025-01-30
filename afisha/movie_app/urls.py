from django.urls import path
from .views import (
    DirectorListCreateAPIView, DirectorDetailAPIView,
    MovieListCreateAPIView, MovieDetailAPIView,
    ReviewListCreateAPIView, ReviewDetailAPIView,
    UserRegisterAPIView, UserConfirmAPIView
)

urlpatterns = [
    path('directors/', DirectorListCreateAPIView.as_view()),
    path('directors/<int:pk>/', DirectorDetailAPIView.as_view()),
    path('movies/', MovieListCreateAPIView.as_view()),
    path('movies/<int:pk>/', MovieDetailAPIView.as_view()),
    path('reviews/', ReviewListCreateAPIView.as_view()),
    path('reviews/<int:pk>/', ReviewDetailAPIView.as_view()),
    path('users/register/', UserRegisterAPIView.as_view()),
    path('users/confirm/', UserConfirmAPIView.as_view()),
]
