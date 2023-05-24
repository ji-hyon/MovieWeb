<template>
  <div>
    <br>
    <select v-model="selectedGenre">
      <option value="">전체</option>
      <option v-for="genre in genres" :value="genre.id" :key="genre.id">{{ genre.name }}</option>
    </select>
    <br><br>
    <button class="w-btn-neon2" @click="recommendMovie">영화 추천</button>
    <br><br>
    <p>
      <RecommendedMovie v-if="randomMovie" :movie="randomMovie" />
    </p>
  </div>
</template>

<script>
import RecommendedMovie from '@/components/RecommendedMovie.vue'

export default {
  name: 'RecommendationView',
  components: {
    RecommendedMovie
  },
  data() {
    return {
      randomMovie: null,
      selectedGenre: '',
    }
  },
  computed: {
    movies() {
      return this.$store.state.movies
    },
    genres() {
      return this.$store.state.genres
    },
  },
  created() {
    this.getMovies()
    this.getGenres()
  },
  methods: {
    getMovies() {
      this.$store.dispatch('getMovies')
    },
    getGenres() {
      this.$store.dispatch('getGenres')
    },
    recommendMovie() {
      let filteredMovies = this.movies;

      if (this.selectedGenre) {
        filteredMovies = this.getMoviesByGenre(this.selectedGenre);
      }

      const highRatedMovies = filteredMovies.filter(movie => movie.vote_average >= 8);

      if (highRatedMovies.length > 0) {
        const randomIndex = Math.floor(Math.random() * highRatedMovies.length);
        this.randomMovie = highRatedMovies[randomIndex];
      } else {
        this.randomMovie = null;
      }
    },
    getMoviesByGenre(genreId) {
      return this.movies.filter(movie => movie.genre_ids.includes(genreId))
    },
  }
}
</script>

<style>
.w-btn-neon2 {
    position: relative;
    border: none;
    min-width: 200px;
    min-height: 50px;

    background: linear-gradient(
    45deg,
    #ff0000,
    #ff7300,
    #fffb00,
    #48ff00,
    #00ffd5,
    #002bff,
    #7a00ff,
    #ff00c8,
    #ff0000
    );
    color: white;
    border-radius: 1000px;
    cursor: pointer;
    box-shadow: 12px 12px 24px rgba(79, 209, 197, 0.64);
    font-weight: 700;
    transition: 0.3s;
    background-size: 400% 400%;
    animation: gradient1 5s ease infinite;
}

.w-btn-neon2:hover {
    transform: scale(1.2);
}

.w-btn-neon2:hover::after {
    content: "";
    width: 30px;
    height: 30px;
    border-radius: 100%;
    border: 6px solid #eee2f2;
    position: absolute;
    z-index: -1;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    animation: ring 1.5s infinite;
}

@keyframes ring {
    0% {
        width: 30px;
        height: 30px;
        opacity: 1;
    }
    100% {
        width: 300px;
        height: 300px;
        opacity: 0;
    }
}

@keyframes gradient1 {
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