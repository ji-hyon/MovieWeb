<template>
  <div>
    <h1>hello, {{ username }}</h1>
    <h2>Liked Movies:</h2>
    <div v-for="movie in likedMovies" :key="movie.id">
      <DetailMovie :movie="movie" />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import DetailMovie from '@/components/DetailMovie.vue'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileView',
  components: {
    DetailMovie
  },
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
    }
  }
}
</script>

<style>

</style>
