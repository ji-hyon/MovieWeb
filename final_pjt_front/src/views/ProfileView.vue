<template>
  <div>
    <h1>hello, {{ username }}</h1>
    <h2>Liked Movies:</h2>
    <div v-for="movie in likedMovies" :key="movie.id">
      <img :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path">
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileView',
  computed: {
    username() {
      return this.$store.state.username
    }
  },
  data() {
    return {
      likedMovies: []
    }
  },

  created() {
    this.getLikedMovies()
  },

  methods: {
    getLikedMovies() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/users/${this.$store.state.username}/liked_movies/`
      })
      .then((res) => {
        this.likedMovies = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },

    getMoviePosterUrl(movie) {
      console.log(movie.poster_path)
      return `${API_URL}${movie.poster_path}`
    }
  }
}
</script>

<style>

</style>
