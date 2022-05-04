from django.urls import path
from .views import ( all_movie, JanrListAPIView,
                    JanrMovieListAPIView,
                    DetailMovieAPIView)




urlpatterns = [
    path('', all_movie),
    path('janr/', JanrListAPIView.as_view()),
    path('janr-movie/<int:pk>/', JanrMovieListAPIView.as_view()),
    path('<int:pk>/', DetailMovieAPIView.as_view()),
]