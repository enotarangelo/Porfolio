from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("portfolio-details", views.portfoliodetails, name="portfolio-details"),
]
