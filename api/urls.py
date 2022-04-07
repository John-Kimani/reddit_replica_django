from django.urls import path
from . import views


urlpatterns = [
    path('post/', views.getData),
    path('add/', views.addArticle),
]