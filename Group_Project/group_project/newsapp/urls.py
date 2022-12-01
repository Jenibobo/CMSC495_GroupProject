from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("sports/", views.Sports, name="sports"),
    path("technology/", views.Technology, name="technology"),
    path("health/", views.Health, name="health"),
    path("science/", views.Science, name="science"),
    path("business/", views.Business, name="business"),
    path("entertainment/", views.Entertainment, name="entertainment"),
] 
