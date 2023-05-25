<template>
  <div class="RecView">
    <br>

    <i class="bi-check2-square"></i>
    <span class="select-word"> 장르를 선택해주세요  :  </span>
    <select v-model="selectedGenre">
      <option value="">전체</option>
      <option v-for="genre in genres" :value="genre.id" :key="genre.id">{{ genre.name }}</option>
    </select>

    <br><br>
    <button class="w-btn-neon2" @click="recommendMovie(); playMusic();">영화 추천</button>
    <br><br>
    <div>
      <RecommendedMovie v-if="randomMovie" :movie="randomMovie" />
    </div>

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

      starAnimationActive: false,
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
      let sum = filteredMovies.reduce((sum, movie) => sum + movie.vote_average, 0)
      const highRatedMovies = filteredMovies.filter(movie => movie.vote_average >= (sum / filteredMovies.length));

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

<style scoped>
.RecView{
  box-shadow: 0 20px 50px rgba(255, 127, 0, 0.3);
}

select {
width: 150px; 
padding: 5px;
border: 2px solid #bc8fec;
font-family: inherit;  
/* background: url('arrow.jpg') no-repeat 95% 50%;  */
border-radius: 10px; 
-webkit-appearance: none; 
-moz-appearance: none;
appearance: none;
color: #9c70ca;
text-align: center;
}

.bi-check2-square{
  color: #5f12a8;
}

.select-word {
  color: #a35fec;
  /* font-weight:bolder */
  font-weight:500
}

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


/* ######################## */
ul{
    margin: 0;
    padding: 0;
}

/* design */

.selectbox{
    margin: 150px auto;
}

.pl{
width: 200px;
border: 1px solid #C4C4C4;
box-sizing: border-box;
border-radius: 10px;
padding: 12px 13px;
font-family: 'Roboto';
font-style: normal;
font-weight: 400;
font-size: 14px;
line-height: 16px;
appearance: none;
text-align: left;
}
.pl:focus{
    border: 1px solid #9B51E0;
    box-sizing: border-box;
    border-radius: 10px;
    outline: 3px solid #F8E4FF;
    border-radius: 10px;
}

.listbox{
    width: 200px;
    list-style: none;
    background: #FFFFFF;
    border: 1px solid #C4C4C4;
    box-sizing: border-box;
    box-shadow: 4px 4px 14px rgba(0, 0, 0, 0.15);
    border-radius: 10px;
    margin-top: 9px;
}

.list{
    border: none;
    background-color: #FFFFFF;
    font-family: 'Roboto';
    font-style: normal;
    font-weight: 400;
    font-size: 14px;
    line-height: 16px;
    padding: 7px 10px;
    margin: 5px 7px;
    box-sizing: border-box;
}

.list:focus{
    background: #F8E4FF;
    width: 184px;
    border-radius: 8px;
    box-sizing: border-box;
    text-align: left;
}

</style>