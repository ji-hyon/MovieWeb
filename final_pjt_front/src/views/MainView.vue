<template>
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
</script>
