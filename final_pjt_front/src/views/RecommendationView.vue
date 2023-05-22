<template>
  <div>
    <button class="btn btn-primary" @click="RecommendMovie">영화 추천</button>
    <br><br>
    <p>
      <RecommendedMovie v-if="randomMovie" :movie="randomMovie" />
    </p>
  </div>
</template>

<script>
import RecommendedMovie from '@/components/RecommendedMovie.vue'

export default {
  name : 'RecommendationView',
  components: {
    RecommendedMovie
  },
  data() {
    return {
      randomMovie: null,
    }
  },
  computed: {
    movies() {
      return this.$store.state.movies
      // return this.$store.state.genreMovies
    }
  },
  methods: {
    RecommendMovie() {
      const randomIndex = Math.floor(Math.random()*this.movies.length)
      this.randomMovie = this.movies[randomIndex]
    }
  }
}
</script>

<style>

</style>
