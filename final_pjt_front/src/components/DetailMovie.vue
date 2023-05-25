<template>
  <div class="detail-page">

  <div class="movie-container">

    <div>
      <!-- 영화 상세 정보 -->
      <div class="details">
          <h1 class="title">{{ movie.title }}</h1>
          <p class="content">{{ movie.overview }}</p>
          <p class="movie-rating"><i class="bi bi-star-fill"></i> {{ movie.vote_average }}</p>
      </div>

      <!-- 유튜브 영상 -->
      <div v-if="youtubeVideo" class="trailer-video">
          <iframe
            :src="'https://www.youtube.com/embed/' + youtubeVideo.videoId"
            width="560"
            height="315"
            frameborder="0"
            allowfullscreen
          ></iframe>
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
const YouTube_API = 'AIzaSyCPYpR-i_hLdrQKnzrV61u0nM1pxp8ci0o'

export default {
    name : 'DetailMovie',
    props: {
      movie : Object
    },
    data() {
      return {
        youtubeVideo: null,
      };
    },

    mounted() {
      this.getYouTubeVideo(this.movie.title)
    },  

    methods: {
      async getYouTubeVideo(title) {
        try {
          const response = await axios.get(
            `https://www.googleapis.com/youtube/v3/search?part=snippet&q=${encodeURIComponent(
              title + ' trailer'
            )}&key=${YouTube_API}`
          );

          const video = response.data.items[0];
          if (video) {
            const videoId = video.id.videoId;
            this.youtubeVideo = { videoId };
          }
        } catch (error) {
          console.error('Failed to fetch YouTube video:', error);
        }
      },
    }

  }

</script>

<style scoped>
.movie-rating {
   color: rgb(153, 78, 153);
   font-weight: bold;
}

.title {
  padding: 20px;
  color: rgb(153, 78, 153);
  font-family: 'Black Han Sans', sans-serif;
}

.movie-container {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: flex-start;
  margin-top: 20px;
  box-shadow: 0 20px 50px rgba(255, 127, 0, 0.3);
}

.trailer-video {
  align-self: flex-end;
  margin-bottom: 100px;
}

.img {
  margin-left: 70px;
  padding-top: 40px;
}

.content {
  width: 600px;
  /* font-family: 'Sunflower', sans-serif; */
  /* font-family: 'IBM Plex Sans KR', sans-serif; */
  font-weight:lighter;
  padding: 30px;
}

.details {
  padding: 20px;
  width: 100%;
  max-width: 600px;
  margin-top: 50px;
}

.bi {
  color: orange;
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