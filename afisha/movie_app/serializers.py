from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Director, Movie, Review

class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.IntegerField(source='movies.count', read_only=True)

    class Meta:
        model = Director
        fields = ['id', 'name', 'movies_count']

class MovieSerializer(serializers.ModelSerializer):
    reviews = serializers.StringRelatedField(many=True)
    rating = serializers.FloatField(source='average_rating', read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'duration', 'director', 'reviews', 'rating']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
