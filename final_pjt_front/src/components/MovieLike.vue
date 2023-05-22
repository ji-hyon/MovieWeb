<template>
  <div>
    <button @click="[movieLike(), getMovieLike()]">
      {{ liked ? '좋아요 취소' : '좋아요' }}
    </button>
    <p>좋아요 : {{ likes_count }}</p>
  </div>
</template>
  
<script>
import axios from "axios"

const API_URL = 'http://127.0.0.1:8000'

export default {
  props:{
    movie: Object,
    movieId: Number,
  },

  data() {
    return {
      likes_count: 0,
      liked: false,
    }
  },

  methods: {
    movieLike() {
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/movies/${this.movieId}/like/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
      .then((res) => {
        this.$emit('get-movie-like')
      })
      .catch((err) => {
        console.log(err)
      })
    },

    getMovieLike() {
      axios({
        method:'get',
        url:`${API_URL}/api/v1/movies/${this.movieId}/like/count`,
        })
        .then((res) => {
          this.likes_count = res.data.likes_count
          this.liked = res.data.liked
        })
        .catch((err) => {
          console.log(err)
      })
    },
  },
}
</script>
