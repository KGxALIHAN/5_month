from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Director, Movie, Review 
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer

class DirectorListAPIView(APIView):
    def get(self, request):
        directors = Director.objects.all()
        data = [{"id": director.id, "name": director.name, "movies_count": director.movies.count()} for director in directors]
        return Response(data)

class DirectorCreateAPIView(CreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class DirectorDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class MovieListAPIView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieCreateAPIView(CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MoviesWithReviewsAPIView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        data = [{
            "id": movie.id,
            "title": movie.title,
            "description": movie.description,
            "duration": movie.duration,
            "director": movie.director.name,
            "reviews": ReviewSerializer(movie.reviews.all(), many=True).data,
            "rating": movie.average_rating()
        } for movie in movies]
        return Response(data)

class ReviewListAPIView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewCreateAPIView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
class re():
    pass