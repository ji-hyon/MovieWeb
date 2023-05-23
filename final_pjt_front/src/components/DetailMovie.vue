<template>
  <div>

  <div class="movie-container">

    <div>
      <div class="details">
          <h1 class="title">{{ movie.title }}</h1>
          <p class="content">{{ movie.overview }}</p>
          <p class="movie-rating"><i class="bi bi-star-fill"></i> {{ movie.vote_average }}</p>
      </div>

      <div v-if="trailerVideoId" class="trailer-video">
        <iframe :src="'https://www.youtube.com/embed/' + trailerVideoId" width="560" height="315" frameborder="0" allowfullscreen></iframe>
      </div>
      <div v-else class="no-trailer">
        <p>No trailer available</p>
      </div>
    </div>

    <div >
      <img class="img" :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path">
    </div>

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


  async mounted() {
    const trailerVideoId = await this.getTrailerVideoId(this.movie.id);
    this.trailerVideoId = trailerVideoId;
  },
  methods: {
    async getTrailerVideoId(movieId) {
      const TMDB_API_KEY = '7708a3b7010d3093206943ce95914382';
      const YOUTUBE_API_KEY = 'AIzaSyCVAuzc4qA4AVqdWLDzd66P694V5T2nI_M';
      
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

  // ###################################################
  // mounted() {
  //   this.searchTrailerVideo();
  // },

  // methods: {
  //   async searchTrailerVideo() {
  //     const YOUTUBE_API_KEY = 'AIzaSyAZrz4levGEeONXL3ffcNANH7teVeM2SI4'; 

  //     const query = `${this.movie.title} ${this.movie.release_date.split('-')[0]} trailer`;
  //     const response = await axios.get(
  //       `https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q=${encodeURIComponent(query)}&key=${YOUTUBE_API_KEY}`
  //     );
  //     this.trailerVideoId = response.data.items[0].id.videoId;
  //   },


  // ######################################################
  // methods: {
  //   async fetchMovies() {
  //     // TMDb API 설정
  //     const TMDB_API_KEY = '7708a3b7010d3093206943ce95914382'; 

  //     const response = await axios.get(
  //       `https://api.themoviedb.org/3/discover/movie?api_key=${TMDB_API_KEY}&language=en-US&sort_by=popularity.desc&include_adult=false`
  //     );
  //     return response.data.results;
  //   },

  //   async searchTrailerVideo(movie) {
  //     // YouTube API 설정
  //     const YOUTUBE_API_KEY = 'AIzaSyAZrz4levGEeONXL3ffcNANH7teVeM2SI4'; 

  //     const query = `${movie.title} ${movie.release_date.split('-')[0]} trailer`;
  //     const response = await axios.get(
  //       `https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q=${encodeURIComponent(query)}&key=${YOUTUBE_API_KEY}`
  //     );
  //     return response.data.items[0].id.videoId;
  //   },
  //   async matchMovieTrailers() {
  //     try {
  //       // 영화 정보와 예고편 정보 매칭하기
  //       const movies = [this.movie]; // movie 데이터를 가져와 배열에 할당하거나 직접 배열로 구성합니다.

  //       // 각 영화에 대해 예고편 동영상 검색 및 매칭
  //       for (const movie of movies) {
  //         const videoId = await this.searchTrailerVideo(movie);
  //         movie.trailer_video_id = videoId; // 예고편 동영상의 Video ID를 해당 영화 데이터에 추가
  //       }

  //       // 예고편 정보를 업데이트하고 화면에 표시
  //       this.trailerVideoId = movies[0].trailer_video_id;
  //     } catch (error) {
  //       console.error('Error:', error.message);
  //     }
  //   },
  // },


  }
</script>

<style scoped>
.title {
  padding: 20px;
  color: rgb(153, 78, 153);
}

.movie-container {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: flex-start;
  margin-top: 20px;
}

.trailer-video {
  align-self: flex-end;
}

.img {
  margin-left: 70px;
}

.content {
  width: 600px;
}

.details {
  padding: 20px;
  width: 100%;
  max-width: 600px;
  margin-top: 50px;
}

/* ########################## */

@media (max-width: 700px) {
  /* 화면이 700px 이하일 때 스타일을 변경 */
  .movie-container {
    flex-direction: column;
    align-items: center;
  }

  .img {
    margin-left: 0;
    margin-top: 20px;
    width: 200px;
    height: auto;
  }

  .content {
    width: 100%;
  }
}

</style>