"""moviebase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from movielist.views import MovieListView, MovieView
from showtimes.views import (
    CinemaListView,
    CinemaView,
    ScreeningListView,
    ScreeningView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', MovieListView.as_view(), name='movie-list'),
    path('movies/<int:pk>/', MovieView.as_view(), name='movie-detail'),
    path('cinemas/', CinemaListView.as_view(), name='cinema-list'),
    path('cinemas/<int:pk>/', CinemaView.as_view(), name='cinema-detail'),
    path('screenings/', ScreeningListView.as_view(), name='screening-list'),
    path('screenings/<int:pk>/', ScreeningView.as_view(),
         name='screening-detail'),
]
