<template>
    <!-- <div class="movie-card">
      <img :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path">
      <div class="movie-info"> -->

    <div>
      <h2>{{ genre }}</h2>
      <ul>
        <li v-for="movie in movies" :key="movie.title">
          {{ movie.title }}
        </li>   
      </ul>

        <router-link
          :to="{
            name: 'DetailView',
            params: { id: movie.id }
          }"
        >
        [Detail]
        </router-link>

        <!-- <p class="movie-overview">{{ movie.overview }}</p>
        <p class="movie-release-date">{{ movie.release_date }}</p>
        <p class="movie-rating">{{ movie.vote_average }}</p> -->
      <!-- </div> -->
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
.movie-cards-container {
  display: flex;
  flex-wrap: wrap;
}

.movie-card {
  width: 300px;
  margin: 20px;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2);
}

.movie-card img {
  width: 100%;
  height: auto;
}

.movie-card .movie-info {
  padding: 20px;
}

.movie-overview {
  white-space: normal;
  display: -webkit-box;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

</style>
