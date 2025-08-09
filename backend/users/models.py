from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=255)

    def __str__(self):
        return f"Profile of {self.user.username}"