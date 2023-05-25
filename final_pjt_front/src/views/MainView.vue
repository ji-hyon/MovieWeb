<template>
  <div>
    <div v-for="genre in genres" :key="genre.pk">
      <br>
      <hr class="divider">

      <div class="genre-wrapper">
        <!-- 푸린이 이미지 -->
        <!-- <img class="img" src= "../assets/char.webp" alt=""> -->
        <h2 class="genre">{{ genre.name }}</h2>
      </div>

      <div class="swiper-container">
        <div class="swiper-wrapper">
          <MovieList v-for="(movie, index) in genre.movies" :key="index" :movie="movie" />
        </div>
        <div class="swiper-pagination"></div>
      </div>
    </div>
  </div>
</template>

<script>
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
        delay: 2500,
        disableOnInteraction: false
      }
    })
  },

  created() {
    this.getMovies()
    this.getGenres()
    this.getMoviesByGenre()
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

    getMoviesByGenre() {
      this.genres.forEach(genre => {
        const moviesByGenre = this.movies.filter(movie => movie.genre_ids.includes(genre.id));
        const selectedMovies = [];

        if (moviesByGenre.length <= 10) {
          genre.movies = moviesByGenre
        } else {
          while (selectedMovies.length < 10) {
            const randomIndex = Math.floor(Math.random() * moviesByGenre.length)
            const randomMovie = moviesByGenre[randomIndex]

            if (!selectedMovies.includes(randomMovie)) {
              selectedMovies.push(randomMovie)
            }
          }
          genre.movies = selectedMovies
        }
      })
    },
  }
}
</script>



<style scoped>
.genre-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
}

.img {
  margin-bottom: 20px;
  height: 50px;
}

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
