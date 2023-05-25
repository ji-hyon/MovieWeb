<template>
  <div>
    <h2>{{ actor.name }}</h2>
    
    <div v-if="error">{{ error }}</div>
    <div v-else>
      <img :src="getActorProfilePath(actor.profile_path)" :alt="actor.name" />
      <ul>
        <li v-for="movie in movies" :key="movie.id">
          {{ movie.title }}
        </li>
      </ul>
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
h2 {
    margin-top: 40px;
    color: rgb(153, 78, 153);
    font-family: 'Black Han Sans', sans-serif;
    padding: 15px;
}
</style>