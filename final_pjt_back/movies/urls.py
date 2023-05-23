from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>/', views.movie_detail),

    path('movies/<int:movie_pk>/comments/', views.comment_list, name='comment_list'),
    path('comments/<int:comment_pk>/', views.comment_detail, name='comment_detail'),
  
    path('genres/', views.genre_list, name='genre_list'),

    # 좋아요 url 작성
    path('movies/<int:movie_pk>/like/<str:username>/', views.like_movie, name='like_movie'),
    path('movies/<int:movie_pk>/liked/users/<str:username>/', views.liked_users, name='liked_users'),
    path('movies/<int:movie_pk>/liked/counts/', views.liked_counts, name='liked_counts'),

    path('users/<str:username>/liked_movies/', views.user_liked_movies, name='user_liked_movies'),
]
