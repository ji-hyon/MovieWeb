<template>
  <div>

  <div class="movie-container">
    <div>
      <h1 class="title">{{ movie.title }}</h1>
      <p class="content">{{ movie.overview }}</p>
    </div>
    <div v-if="trailerVideoId" class="trailer-video">
      <iframe :src="'https://www.youtube.com/embed/' + trailerVideoId" width="560" height="315" frameborder="0" allowfullscreen></iframe>
    </div>
    <div v-else class="no-trailer">
      <p>No trailer available</p>
    </div>

    <img :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path">
    <div class="details">
    </div>
    <p class="movie-rating"><i class="bi bi-star-fill"></i> {{ movie.vote_average }}</p>

  </div>


  </div>
</template>

<script>
import axios from 'axios'

export default {
    name : 'DetailMovie',
    props: {
      movie : Object
    },
    data() {
    return {
      trailerVideoId: null
    };
  },


  // 유튜브 영상 관련 코드
  async mounted() {
    const trailerVideoId = await this.getTrailerVideoId(this.movie.id);
    this.trailerVideoId = trailerVideoId;
  },
  methods: {
    async getTrailerVideoId(movieId) {
      const TMDB_API_KEY = '7708a3b7010d3093206943ce95914382';
      const YOUTUBE_API_KEY = 'AIzaSyAZrz4levGEeONXL3ffcNANH7teVeM2SI4';

      const tmdbResponse = await axios.get(
        `https://api.themoviedb.org/3/movie/${movieId}?api_key=${TMDB_API_KEY}`
      );
      const movie = tmdbResponse.data;

      const keyword = `${movie.title} 예고편`;
      const youtubeResponse = await axios.get(
        `https://www.googleapis.com/youtube/v3/search?part=snippet&q=${encodeURIComponent(keyword)}&key=${YOUTUBE_API_KEY}`
      );

      const videos = youtubeResponse.data.items;
      const trailer = videos.find(video => video.id.kind === 'youtube#video');

      if (trailer) {
        return trailer.id.videoId;
      } else {
        return null;
      }
    }
  }

}
</script>

<style scoped>
.movie-container {

}

</style>