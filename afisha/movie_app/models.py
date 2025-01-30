from django.db import models
import random
from django.contrib.auth.models import User

class Director(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.PositiveIntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')

    def average_rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            return sum(review.stars for review in reviews) / reviews.count()
        return 0

    def __str__(self):
        return self.title


class UserConfirmation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="confirmation")
    code = models.CharField(max_length=6, unique=True)

    def generate_code(self):
        self.code = f"{random.randint(100000, 999999)}"
        self.save()


class Review(models.Model):
    text = models.TextField()
    stars = models.PositiveIntegerField(default=1)  # Рейтинг от 1 до 5
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f'Review for {self.movie.title}'
