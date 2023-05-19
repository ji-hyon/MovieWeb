<template>
  <div class="d-flex flex-wrap justify-content-center">
    <MovieList 
     v-for="movie in movies" 
     :key="movie.id"
     :movie ="movie" />
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
    }
  },

  methods: {
    getMovies() {
      this.$store.dispatch('getMovies')
    }
  }
}
</script>
