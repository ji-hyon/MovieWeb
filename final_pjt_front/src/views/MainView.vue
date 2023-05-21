<template>
  <div class="d-flex flex-wrap justify-content-center">
    <MovieList 
     v-for="movie in movies" 
     :key="movie.id"
     :movie ="movie" />
  <!-- <MovieList v-for="(movies, genre) in genreMovies" :key="genre" :movies="movies" :genre="genre" /> -->
  </div>
</template>

<script>
import MovieList from '@/components/MovieList.vue'

export default {
  name: 'MainView',
  components: {
    MovieList,
  },

  created() {
    this.getMovies()
  },

  computed: {
    movies() {
      return this.$store.state.movies
      // return this.$store.state.genreMovies
    }
  },

  methods: {
    getMovies() {
      this.$store.dispatch('getMovies')
    }
  }
}
</script>
