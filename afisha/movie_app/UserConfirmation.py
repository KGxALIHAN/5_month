import random
from django.contrib.auth.models import User
from django.db import models

class UserConfirmation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="confirmation")
    code = models.CharField(max_length=6, unique=True)

    def generate_code(self):
        self.code = f"{random.randint(100000, 999999)}"
        self.save()
