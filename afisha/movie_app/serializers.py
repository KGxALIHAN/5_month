from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Director, Movie, Review, UserConfirmation

class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.IntegerField(source='movies.count', read_only=True)

    class Meta:
        model = Director
        fields = ['id', 'name', 'movies_count']


class MovieSerializer(serializers.ModelSerializer):
    rating = serializers.FloatField(source='average_rating', read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'duration', 'director', 'rating']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'text', 'stars', 'movie']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            is_active=False
        )
        confirmation = UserConfirmation.objects.create(user=user)
        confirmation.generate_code()
        return user
