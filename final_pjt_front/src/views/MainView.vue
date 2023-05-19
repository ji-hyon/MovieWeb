<template>
  <div class="main">
    <h1>Main Page</h1>
    <MovieList/>
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
  methods: {
    getMovies() {
      this.$store.dispatch('getMovies')
    }
  }
}
</script>
