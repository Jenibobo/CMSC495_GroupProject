from django.urls import path
from . import views

urlpatterns = [
    path('', views.weather),
    # path('', views.news_feed)
]