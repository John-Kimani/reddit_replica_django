from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=15)


class Article(models.Model):
    title = models.CharField(max_length=40)
    article = models.TextField(default='Uploaded')
    editor = models.ForeignKey(User, default=1, on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


class Room(models.Model):
    name = models.CharField(max_length=20)