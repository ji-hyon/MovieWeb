<template>
    <div class="movie-card">
      <img :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path">
      <div class="movie-info">
        <h2 class="movie-title">{{ movie.title }}</h2>
        <p class="movie-overview">{{ movie.overview }}</p>
        <p class="movie-release-date">{{ movie.release_date }}</p>
        <p class="movie-rating">{{ movie.vote_average }}</p>
      </div>
    </div>
</template>

<script>
// import MovieListItem from '@/components/MovieListItem'

export default {
  name: 'MovieList',
  props: {
    movie: {
      type: Object,
      required: true,
    },
  },
}
</script>

<style>
.movie-list {
  text-align: start;
}
</style>
