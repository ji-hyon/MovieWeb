<template>
  <div class="profileView">

    <h1 class="name">Hello, {{ username }}</h1>

    <h2 class="like"><i class="bi-suit-heart-fill"></i>&nbsp; Liked Movies:</h2>
    <div class="movies">
      <div class="image-container"> 
        <!-- <div v-for="movie in likedMovies" :key="movie.id"> -->
        <router-link class="link" v-for="movie in likedMovies" :key="movie.id" :to="'/' + movie.id">
          <img class="img" :src="getMoviePosterUrl(movie)">
        <!-- </div> -->
        </router-link>
      </div>
    </div>
    
    <div class="comment-area">
      <h2 class="like"><i class="bi-chat-right-text-fill"></i>&nbsp; Comments:</h2>
      <div v-for="comment in getUserComments" :key="comment.id">

        <div class="comment">
          <span class="movie-link">
            <router-link :to="{ name: 'DetailView', params: { id: comment.movie }}">
              <img class="poster-img" :src="getMoviePosterImg(comment.movie)" :alt="getMovieTitle(comment.movie)">
              {{ getMovieTitle(comment.movie) }}
            </router-link>
            &nbsp;&nbsp;|&nbsp;&nbsp;
            <span class="comment-content">"{{ comment.content }}"</span>
          </span>
        </div>
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

    getMoviePosterImg(movieId) {
      const movie = this.$store.state.movies[movieId-1]
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
.profileView {
  box-shadow: 0 20px 50px rgba(255, 127, 0, 0.3);
}
.comment {
  display: flex;
  margin: 20px;
  margin-left: 80px;
  color: rgb(153, 78, 153);
  font-size: 17px;
}

.comment-content {
  font-weight: bold;
  /* color: rgb(145, 41, 145); */
}

.name {
  color: rgb(153, 78, 153);
  font-family: 'Black Han Sans', sans-serif;
  padding: 15px;
  margin-top: 30px;
}

.like {
  /* color: rgb(153, 78, 153); */
  color: rgb(171, 57, 171);
  /* margin-left: 20%; */
  margin-right: 60%;
}

.bi-suit-heart-fill{
  color: rgb(233, 135, 233);
}

.bi-chat-right-text-fill{
  color: rgb(213, 116, 213);
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

.comment-area {
  padding: 30px;
  margin-bottom: 50px;
}

.poster-img {
  width: 30px;
}
</style>