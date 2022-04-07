from django.db import models
from django.contrib.auth.models import User
from users.models import Profile

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=40)
    article = models.TextField(default='Uploaded')
    editor = models.ForeignKey(Profile, default=1, on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Room(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name