<template>
  <div class="actorView">
    <h2 class="actor"><i class="bi-person-square"></i>&nbsp; Actors</h2>
    <div v-if="error">{{ error }}</div>
    <div class="actors" v-else>
        <span v-for="actor in actors.slice(0, 5)" :key="actor.id">
          <img class="img" :src="getActorProfilePath(actor.profile_path)" :alt="actor.name" />
          <p>{{ actor.name }}</p>
        </span>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
 name: "ActorsData",
 props: ['movie'],

 data() {
    return {
      actors: [],
      error: null
    };
  },
  mounted() {
    this.fetchActors();
  },
  methods: {
    async fetchActors() {
      try {
        const response = await axios.get(`https://api.themoviedb.org/3/movie/${this.movie.movie_id}/credits`, {
          params: {
            api_key: '7708a3b7010d3093206943ce95914382'
          }
        });
        this.actors = response.data.cast;
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
    }
  }


}
</script>

<style>
.actorView {
  box-shadow: 0 20px 50px rgba(255, 127, 0, 0.3);
}

.actor {
  padding: 20px;
  color: rgb(153, 78, 153);
  font-family: 'Black Han Sans', sans-serif;
}

.actors {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.img {
  display: block;
  margin: 10px;
}
</style>