from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import Director, Movie, Review, UserConfirmation
from .serializers import (
    DirectorSerializer, MovieSerializer, ReviewSerializer, RegisterSerializer
)

class DirectorListCreateAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class DirectorDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class MovieListCreateAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MoviesWithReviewsAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def list(self, request, *args, **kwargs):
        movies = self.get_queryset()
        data = [
            {
                "id": movie.id,
                "title": movie.title,
                "description": movie.description,
                "duration": movie.duration,
                "director": movie.director.name,
                "reviews": ReviewSerializer(movie.reviews.all(), many=True).data,
                "rating": movie.average_rating()
            }
            for movie in movies
        ]
        return Response(data)

class ReviewListCreateAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class RegisterAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class ConfirmUserAPIView(APIView):
    def post(self, request):
        code = request.data.get('code')
        try:
            confirmation = UserConfirmation.objects.get(code=code)
            user = confirmation.user
            user.is_active = True
            user.save()
            confirmation.delete()
            return Response({"message": "Пользователь успешно подтвержден."}, status=status.HTTP_200_OK)
        except UserConfirmation.DoesNotExist:
            return Response({"error": "Неверный код подтверждения."}, status=status.HTTP_400_BAD_REQUEST)
