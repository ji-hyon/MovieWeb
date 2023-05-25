<template>
  <div>

    <div class="actor-area">
    <!-- <div> -->
      <h2><i class="bi bi-person-heart"></i>&nbsp;&nbsp;{{ actor.name }}</h2>
      
      <div v-if="error">{{ error }}</div>
      <div v-else>
        <div class="actor">
          <div class="test">
          <img class="actor-img" :src="getActorProfilePath(actor.profile_path)" :alt="actor.name" />
          </div>
        </div>
      <!-- </div> -->
    </div>
    </div>

      <br><br>
      <div class="movies">
        <h2 class="m"><i class="bi-film"></i>&nbsp; Movies</h2>
        <div class="image-container">
          <div v-for="movie in movies" :key="movie.id">
            <p class="title">{{ movie.title }}</p>
            <img class="img" :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path">
          </div>
       </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios'

export default {
    name: "ActorDetailView",

    data() {
    return {
      actor: null,
      movies: [],
      error: null,
    };
  },
  mounted() {
    this.fetchActor();
  },
  methods: {
    async fetchActor() {
      const actorId = this.$route.params.id;
      try {
        const actorResponse = await axios.get(`https://api.themoviedb.org/3/person/${actorId}`, {
          params: {
            api_key: '7708a3b7010d3093206943ce95914382',
          },
        });
        this.actor = actorResponse.data;

        const moviesResponse = await axios.get(`https://api.themoviedb.org/3/person/${actorId}/movie_credits`, {
          params: {
            api_key: '7708a3b7010d3093206943ce95914382',
          },
        });
        this.movies = moviesResponse.data.cast;
      } catch (err) {
        this.error = err.message;
      }
    },
    getActorProfilePath(profilePath) {
      if (profilePath) {
        return `https://image.tmdb.org/t/p/w200${profilePath}`;
      } else {
        return ''; // 기본 이미지나 대체할 내용 설정
      }
    },
  },
}
</script>

<style scoped>
.m {
  padding-top: 60px;
  padding-bottom: 40px;
}

.actor-area{
  margin-top: 30px;
  padding: 40px;
  box-shadow: 0 20px 50px rgba(255, 127, 0, 0.3);
}

.movies{
  box-shadow: 0 20px 50px rgba(255, 127, 0, 0.3);
  margin-bottom: 100px;
}

h2 {
    color: rgb(153, 78, 153);
    font-family: 'Black Han Sans', sans-serif;
    padding: 15px;
}
.title {
  font-weight: bold;
  color: rgb(153, 78, 153);
}


.img {
  width: 200px;
}

.image-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.actor{
  display: flex;
  justify-content: center;
}

.test {
  width: 200px;
  --borderWidth: 7px;
  background: #e3c2e5;
  position: relative;
  border-radius: var(--borderWidth);
  margin-bottom: 25px;
}

.test:after {
  content: '';
  position: absolute;
  top: calc(-1 * var(--borderWidth));
  left: calc(-1 * var(--borderWidth));
  height: calc(100% + var(--borderWidth) * 2);
  width: calc(100% + var(--borderWidth) * 2);
  background: linear-gradient(60deg, #f79533, #f37055, #ef4e7b, #a166ab, #5073b8, #1098ad, #07b39b, #6fba82);
  border-radius: calc(2 * var(--borderWidth));
  z-index: -1;
  animation: animatedgradient 3s ease alternate infinite;
  background-size: 300% 300%;
}


@keyframes animatedgradient {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}

</style>