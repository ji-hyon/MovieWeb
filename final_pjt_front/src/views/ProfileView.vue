<template>
  <div>
    <h1 class="name">Hello, {{ username }}</h1>
    <h2 class="like"><i class="bi-suit-heart-fill"></i>&nbsp; Liked Movies:</h2>
    <div class="image-container"> 
      <!-- <div v-for="movie in likedMovies" :key="movie.id"> -->
      <router-link v-for="movie in likedMovies" :key="movie.id" :to="'/' + movie.id">
        <img class="img" :src="getMoviePosterUrl(movie)">
      <!-- </div> -->
      </router-link>
    </div>

    <h2 class="like">Comments:</h2>
    <div v-for="comment in getUserComments" :key="comment.id">
      <p>{{ comment.user.username }}</p>
      <p>{{ getMovieTitle(comment.movie) }}</p>
      <p>{{ comment.content }}</p>
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
    },
    getUserComments() {
      return this.comments.filter(comment => comment.user.username === this.username)
    }
  },
  data() {
    return {
      likedMovies: [],
      comments: []
    }
  },
 
  created() {
    this.getLikedMovies()
    this.getAllComments()
  },

  methods: {
    getLikedMovies() {
      axios.get(`${API_URL}/api/v1/users/${this.username}/liked_movies/`)
        .then((res) => {
          this.likedMovies = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },

    getAllComments() {
      axios.get(`${API_URL}/api/v1/movies_comment/`)
        .then((res) => {
          this.comments = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },

    getMoviePosterUrl(movie) {
      return `https://image.tmdb.org/t/p/w500${movie.poster_path}`
    },

    getMovieTitle(movieId) {
      const movie = this.$store.state.movies[movieId-1]
      return movie ? movie.title : 'Unknown'
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