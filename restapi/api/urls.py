from django.urls import path
from . views import articleView
from . models import Article
from . import models

urlpatterns = [
    path('articles/', articleView.as_view())
]