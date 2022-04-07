from django.urls import path
from . import views


urlpatterns = [
    path('post/', views.getData, name='post'),
    path('add/', views.addArticle, name='add'),
]