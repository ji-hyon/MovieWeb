<template>

  <div>
    <div v-for="genre in genres" :key="genre.pk">
      <br>
      <hr class="divider">
      <h2 class="genre">{{ genre.name }}</h2>
        <div class="swiper-container">
          <div class="swiper-wrapper">

              <!-- <MovieList v-for="(movie, index) in getMoviesByGenre(genre.id).slice(0, 5)" :key="index" :movie="movie" /> -->
              <MovieList v-for="(movie, index) in getMoviesByGenre(genre.id, 5)" :key="index" :movie="movie" />

          </div>
        <!-- <div class="swiper-pagination"></div> -->
        <swiper-pagination class="swiper-pagination"></swiper-pagination>
        </div>
      </div>
  </div>


</template>

<script>
// import "../public/script.js"
import Swiper from 'swiper'
import MovieList from '@/components/MovieList.vue'

export default {
  name: 'MainView',
  components: {
    MovieList,
  },

  mounted() {
  new Swiper('.swiper-container', {
    slidesPerView: 'auto',
    initialSlide: 2,
    speed: 1000,
    spaceBetween: 32,
    loop: true,
    centeredSlides: true,
    roundLengths: true,
    mousewheel: true,
    grabCursor: true,
    pagination: {
      el: '.swiper-pagination',
      clickable: true
    },
    autoplay: {
      delay: 2500, // 3초마다 슬라이드 전환
      disableOnInteraction: false // 사용자 상호작용 후에도 자동재생 유지
    }
  });
},

  created() {
    this.getMovies()
    this.getGenres()
  },

  computed: {
    movies() {
      return this.$store.state.movies
    },
    genres() {
      return this.$store.state.genres
    },
  },

  methods: {
    getMovies() {
      this.$store.dispatch('getMovies')
    },
    getGenres() {
      this.$store.dispatch('getGenres')
    },
    // getMoviesByGenre(genreId) {
    //   return this.movies.filter(movie => movie.genre_ids.includes(genreId))
    // },
    getMoviesByGenre(genreId, count) {
      const moviesByGenre = this.movies.filter(movie => movie.genre_ids.includes(genreId));
      const randomMovies = [];
      const totalMovies = moviesByGenre.length;

      if (count >= totalMovies) {
        return moviesByGenre; // 장르에 속한 모든 영화를 반환
      }

      while (randomMovies.length < count) {
        const randomIndex = Math.floor(Math.random() * totalMovies);
        const randomMovie = moviesByGenre[randomIndex];

        if (!randomMovies.includes(randomMovie)) {
          randomMovies.push(randomMovie);
        }
      }

      return randomMovies;
    },

    chunkedMoviesByGenre(genreId, size) {
    const moviesByGenre = this.getMoviesByGenre(genreId)
    const chunkedArray = []
    let chunk = []
    for (let i = 0; i < moviesByGenre.length; i++) {
      chunk.push(moviesByGenre[i])
      if (chunk.length === size || i === moviesByGenre.length - 1) {
        chunkedArray.push(chunk)
        chunk = []
      }
    }
    return chunkedArray
  },


  }
}
</script>

<style scoped>

*, ::after, ::before {
  box-sizing: unset;
}

.genre {
  color: rgb(153, 78, 153);
  font-family: 'Black Han Sans', sans-serif;
  padding: 15px;
}

.divider {
  /* background: linear-gradient(to right, transparent, red, orange, yellow, green, blue, indigo, violet, transparent); */
  background: linear-gradient(45deg, #ff0000,#ff7300, #fffb00, #48ff00,#00ffd5, #002bff, #7a00ff, #ff00c8,#ff0000);
  animation: gradient1 5s ease infinite;
  height: 7px;
  margin: 20px 0;
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

.swiper-container {
  height: 400px;
  width: 100%;
  padding-bottom: 85px;
}

.swiper-wrapper {
  width: 73.8%;
  will-change: transform;
}
@media (min-width: 630px) {
  .swiper-wrapper {
    /* width: 100%; */
  }
}

.swiper-slide {
  width: 100%;
  background-color: white;
  overflow: hidden;
}
.swiper-slide.swiper-slide-active .slide-image, .swiper-slide.swiper-slide-duplicate-active .slide-image {
  transform: scale3d(1, 1, 1);
}
@media (min-width: 630px) {
  .swiper-slide {
    width: 50%;
  }
}
@media (min-width: 768px) {
  .swiper-slide {
    width: 33.333333%;
  }
  .swiper-slide.swiper-slide-next .slide-image, .swiper-slide.swiper-slide-prev .slide-image, .swiper-slide.swiper-slide-duplicate-next .slide-image, .swiper-slide.swiper-slide-duplicate-prev .slide-image {
    transform: scale3d(1, 1, 1);
  }
}
@media (min-width: 1024px) {
  .swiper-slide {
    width: 25%;
  }
}

.swiper-pagination {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 85px;
}
.swiper-pagination.swiper-pagination {
  bottom: 0;
}

.swiper-pagination-bullet {
  background: tomato;
  width: 22px;
  height: 4px;
  border-radius: 0;
  transition: opacity 1s ease;
}
.swiper-pagination-bullet.swiper-pagination-bullet.swiper-pagination-bullet {
  margin: 0;
}
@media (min-width: 768px) {
  .swiper-pagination-bullet {
    width: 40px;
  }
}

.slide-image {
  height: 100%;
  width: 100%;
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  transform: scale3d(1.3, 1.3, 1);
  backface-visibility: hidden;
  will-change: transform;
  transition: transform 1400ms ease;
}

.slide-content {
  padding: 0 2.2rem;
  display: flex;
  flex-direction: column;
  height: 100%;
}
.slide-content h4 {
  font-size: 25px;
  font-weight: 400;
  margin: 0 0 1rem;
  padding-top: 2.8rem;
  flex-grow: 0;
}
.slide-content p {
  display: flex;
  line-height: 1.8;
  margin-top: 0;
  font-size: 14px;
  flex-grow: 1;
}
.slide-content footer {
  display: flex;
  justify-content: space-between;
  width: 100%;
  padding-bottom: 2.8rem;
  font-size: 14px;
  color: #c2c0e0;
}
.slide-content a {
  color: tomato;
  font-size: 12px;
  font-weight: 700;
  text-decoration: none;
  border-bottom: 3px solid currentColor;
  padding-bottom: 3px;
}

.bi {

}

</style>



<!--###################### 페이지 ############################-->
<!-- <template>
  <div>
    <div class="d-flex flex-wrap justify-content-center">
      <div class="d-flex flex-wrap justify-content-center">
        <div v-for="(row, index) in paginatedMovies" :key="index" class="d-flex flex-wrap justify-content-center">
          <div v-for="movie in row" :key="movie.id" class="w-25">
            <MovieList :movie="movie" />
          </div>
        </div>
      </div>
    </div>

    <div class="d-flex justify-content-center mt-3">
      <v-pagination v-model="currentPage" :page-count="totalPages" />
    </div>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList.vue'
import vPagination from 'vue-plain-pagination'

export default {
  name: 'MainView',
  components: {
    MovieList,
    vPagination,
  },
  data() {
    return {
      currentPage: 1,
      itemsPerPage: 8,
      moviesPerRow: 4,
      rowsPerPage: 2,
    }
  },
  computed: {
    movies() {
      return this.$store.state.movies
    },
    totalPages() {
      return Math.ceil(this.movies.length / this.itemsPerPage)
    },
    paginatedMovies() {
      const startIndex = (this.currentPage - 1) * this.itemsPerPage
      const endIndex = startIndex + this.itemsPerPage
      const slicedMovies = this.movies.slice(startIndex, endIndex)
      return this.chunkArray(slicedMovies, this.moviesPerRow).slice(0, this.rowsPerPage)
    },
  },
  created() {
    this.getMovies()
  },
  methods: {
    getMovies() {
      this.$store.dispatch('getMovies')
    },
    chunkArray(array, size) {
      const chunkedArray = []
      for (let i = 0; i < array.length; i += size) {
        const chunk = array.slice(i, i + size)
        chunkedArray.push(chunk)
      }
      return chunkedArray
    },
  },
}
</script> -->
