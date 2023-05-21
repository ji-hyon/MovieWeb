<template>
  <div>
    <div class="d-flex flex-wrap justify-content-center">
      <MovieList
        v-for="movie in paginatedMovies"
        :key="movie.id"
        :movie="movie"
      />
    </div>

    <div class="d-flex justify-content-center mt-3">
      <v-pagination v-model="currentPage" :page-count="totalPages" />
    </div>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList.vue'
import vPagination from 'vue-plain-pagination'

// 참고 : https://vuejsexamples.com/pagination-component-for-vue-js-2/

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
      return this.movies.slice(startIndex, endIndex)
    },
  },
  created() {
    this.getMovies()
  },
  methods: {
    getMovies() {
      this.$store.dispatch('getMovies')
    },
  },
}
</script>
