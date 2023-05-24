<template>
  <div>
    <h1 class="name">Hello, {{ username }}</h1>
    <!-- <h2 class="like">Liked Movies:</h2> -->
    <h2 class="like"><i class="bi-suit-heart-fill"></i>&nbsp; Liked Movies:</h2>
    <div class="image-container"> 
      <div v-for="movie in likedMovies" :key="movie.id">
        <img class="img" :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path">
      </div>
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

<style scoped>
.name {
  color: rgb(153, 78, 153);
  font-family: 'Black Han Sans', sans-serif;
  padding: 15px;
  margin-top: 30px;
}

.like{
  color: rgb(153, 78, 153);
  margin-left: 20%;
  margin-bottom: 30px;
  /* font-family: 'Black Han Sans', sans-serif; */
}

.bi-suit-heart-fill{
  color: rgb(233, 135, 233);
}

.img {
  width: 300px;
  margin: 30px;
}

.image-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}
</style>
