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

      // 필터링된 영화 중 평점이 8점 이상인 영화들로 필터링
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