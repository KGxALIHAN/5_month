from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer

# Список режиссёров
class DirectorListAPIView(APIView):
    def get(self, request):
        directors = Director.objects.all()
        data = []
        for director in directors:
            data.append({
                "id": director.id,
                "name": director.name,
                "movies_count": director.movies.count()  # Подсчёт фильмов
            })
        return Response(data)


# Детальная информация о режиссёре
class DirectorDetailAPIView(RetrieveAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


# Список фильмов
class MovieListAPIView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


# Детальная информация о фильме
class MovieDetailAPIView(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


# Список фильмов с отзывами и средней оценкой
class MoviesWithReviewsAPIView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        data = []
        for movie in movies:
            data.append({
                "id": movie.id,
                "title": movie.title,
                "description": movie.description,
                "duration": movie.duration,
                "director": movie.director.name,
                "reviews": ReviewSerializer(movie.reviews.all(), many=True).data,
                "rating": movie.average_rating()  # Средний рейтинг фильма
            })
        return Response(data)


# Список отзывов
class ReviewListAPIView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


# Детальная информация об отзыве
class ReviewDetailAPIView(RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
