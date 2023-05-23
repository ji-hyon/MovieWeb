from rest_framework.response import Response
from rest_framework.decorators import api_view
# Authentication Decorators
# from rest_framework.decorators import authentication_classes

# permission Decorators
# from rest_framework.decorators import permission_classes
# from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import MovieListSerializer, MovieSerializer, CommentSerializer, GenreSerializer
from .models import Movie, Comment, Genre
from accounts.models import User


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def movie_list(request):
    if request.method == 'GET':
        # movies = Movie.objects.all()
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MovieListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def movie_detail(request, movie_pk):
    # movie = Movie.objects.get(pk=movie_pk)
    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        print(serializer.data)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['POST', 'GET'])
def comment_list(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    elif request.method == 'GET':
        comments = movie.comment_set.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    # comments = Comment.objects.filter(movie_id=movie_pk)
    # serializer = CommentSerializer(comments, many=True)
    # return Response(serializer.data)

@api_view(['GET'])
def genre_list(request):
    genres = get_list_or_404(Genre)
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)
    
@api_view(['POST'])
def like_movie(request, movie_pk, username):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = get_object_or_404(User, username=username)

    if movie.liked_users.filter(pk=user.pk).exists():
        movie.liked_users.remove(user)
    else:
        movie.liked_users.add(user)

    serializer = MovieListSerializer(movie)
    data = {'movie': serializer.data}
    return Response(data)

@api_view(['GET'])
def liked_users(request, movie_pk, username):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = get_object_or_404(User, username=username)

    liked = movie.liked_users.filter(pk=user.pk).exists()

    data = {'liked': liked}
    return Response(data)


@api_view(['GET'])
def liked_counts(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    likes_count = movie.liked_users.count()

    data = {'likes_count': likes_count}
    return Response(data)

from accounts.models import User

@api_view(['GET'])
def user_liked_movies(request, username):
    user = get_object_or_404(User, username=username)
    movies = Movie.objects.filter(liked_users=user)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def comment_update(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)