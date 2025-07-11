from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    email = models.EmailField(unique=True)


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
