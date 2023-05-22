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
    path('movies/<int:movie_pk>/like/count/<str:username>/', views.like_movie_users, name='like_movie_users'),
    path('movies/<int:movie_pk>/likes/counts/', views.like_movie_count, name='like_movie_count'),    
]
