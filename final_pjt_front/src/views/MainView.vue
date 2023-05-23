<template>

  <div>
    <div v-for="genre in genres" :key="genre.pk">
      <br>
      <h2 class="genre">{{ genre.name }}</h2>
      <div class="row justify-content-center">
        <div class="col-sm-2 mb-3" v-for="(movie, index) in getMoviesByGenre(genre.id).slice(0, 4)" :key="index">
          <MovieList :movie="movie" />
        </div>
      </div>
    </div>
  </div>

</template>

<script>
import MovieList from '@/components/MovieList.vue'

export default {
  name: 'MainView',
  components: {
    MovieList,
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
    getMoviesByGenre(genreId) {
      return this.movies.filter(movie => movie.genre_ids.includes(genreId))
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

<style>
.genre {
  color: rgb(153, 78, 153);
  font-family: 'Black Han Sans', sans-serif;
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
